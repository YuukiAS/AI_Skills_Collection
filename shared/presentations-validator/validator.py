"""Offline PDF deck validation. Verdicts depend on visible content, never file identity."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import statistics
import time
from collections import Counter, defaultdict
from itertools import pairwise
from pathlib import Path

import measure
import numpy as np
import pymupdf as pdf
import yaml

ROOT = Path(__file__).resolve().parent
DATE = re.compile(
    r"(?:\b(?:19|20)\d{2}\s*[-/.年]\s*\d{1,2}\s*[-/.月]\s*\d{1,2}\s*日?|\b\d{1,2}\s+(?:Jan\w*|Feb\w*|Mar\w*|Apr\w*|May|Jun\w*|Jul\w*|Aug\w*|Sep\w*|Oct\w*|Nov\w*|Dec\w*)\s+(?:19|20)\d{2}\b|\b(?:Jan\w*|Feb\w*|Mar\w*|Apr\w*|May|Jun\w*|Jul\w*|Aug\w*|Sep\w*|Oct\w*|Nov\w*|Dec\w*)\s+\d{1,2},?\s+(?:19|20)\d{2}\b)",
    re.IGNORECASE,
)
QUESTION = re.compile(
    r"^(?:Questions?\s*[?？]?|Q\s*&\s*A|讨论\s*[?？]?|问题\s*[?？]?)$", re.IGNORECASE
)
AUDIT = re.compile(
    r"\b(?:sha[- ]?(?:256|512)|md5|receipt|READY_FOR_\w+|NOT_RUN|AUDIT[_ -]?(?:PASS|TRAIL)|[a-f0-9]{32,64})\b|(?-i:\b(?:PASS|FAIL)\b)|哈希|收据|已核对|已检查|已校验|已验收|本页已|验收通过|按合同|任务合同|执行合同|已完成审计",
    re.IGNORECASE,
)
PATH = re.compile(
    r"(?:[A-Za-z]:[\\/][^\s]+|(?:~?/|\./|\.\./)(?:[\w.~-]+/)+[^\s,;]+|\b[\w.-]+\.(?:tex|pdf|csv|json|ya?ml|log|py|md)\b)",
    re.IGNORECASE,
)
VERSION = re.compile(
    r"\b(?:internal|draft|revision|rev|deck|candidate|build|version)\s*[-_:]?\s*v?\d+(?:\.\d+)*\b|内部版本|(?:修订版|内部版)\s*\d+|\bv\d+(?:\.\d+)*\b",
    re.IGNORECASE,
)
CONTRAST = re.compile(
    r"不是[^。！？\n]{1,100}而是|并非[^。！？\n]{1,100}而是|\bnot\s+[^.!?\n]{1,100}?\s+but\s+(?!also\b)",
    re.IGNORECASE,
)
RUNTIME = re.compile(
    r"耗时|运行时间|计算时间|\b(?:runtime|wall[- ]?time|elapsed|GPU[- ]hours?|CPU[- ]hours?)\b|\b\d+(?:\.\d+)?\s*(?:ms|seconds?|minutes?|hours?)\b",
    re.IGNORECASE,
)
DATA_VERSION = re.compile(
    r"数据版本|数据版次|来源核对|\b(?:dataset|data|source)\s*(?:version|release|revision|accounting)\b|\bv\d+(?:\.\d+)*\b",
    re.IGNORECASE,
)
SOURCE = re.compile(
    r"^(?:Data|Source|Sources|Credit|Photo|Reference|References|数据|来源|参考|图片来源)\s*[:：]|doi\s*:|https?://|\b10\.\d{4,9}/|\[\d+\]",
    re.IGNORECASE,
)
ABBR = re.compile(
    r"(?<![A-Za-z0-9])(?:[A-Z]&[A-Za-z]+|[A-Z][a-z]+[A-Z][A-Za-z]*|[A-Z]{2,}[a-z]?)(?:-(?:[A-Z]{2,}[a-z]?|[A-Z][a-z]+[A-Z][A-Za-z]*|[0-9]+(?:\.[0-9]+)*))*"
)


def rules(path=ROOT / "rules.yaml"):
    data = yaml.safe_load(Path(path).read_text())
    rows = data["rules"]
    if len({r["id"] for r in rows}) != len(rows):
        raise ValueError("Duplicate rule ID")
    for r in rows:
        if r["mode"] not in {"auto", "partial", "judged"}:
            raise ValueError(f"Unknown mode: {r['id']}")
        if r["mode"] != "judged" and not callable(globals().get(r["detector"])):
            raise ValueError(f"Missing detector: {r['id']}")
    return rows


def measurement_config():
    return {
        "limits": {
            "boundary_px": 2,
            "optical_px": 2,
            "short_token_chars": 8,
            "font_tolerance_pt": 0.1,
            "column_bottom_review_px": 100,
        },
        "font_pdf_pt": {"body": 10.959, "caption": 7.97, "code": 7.97, "table": 9.963},
        "font_tex_baselines_pt": {"body": 13.5, "code": 9.6, "caption": 9.6},
        "list_contract": {"teaching_list_itemsep_tex_pt_range": [1.15, 7]},
        "semantic_spacing": {"caption_to_body": {"target": [6, 12]}},
        "column_presets": {
            "symmetric": [0.48, 0.48],
            "left_wide": [0.57, 0.39],
            "right_wide": [0.39, 0.57],
        },
        "_extraction": {"chromatic_color_range_min": 0.05, "white_fill_min": 0.98},
    }


def result(page, evidence, status="FAIL", **details):
    return {
        "page": page["number"],
        "status": status,
        "evidence": evidence,
        "details": details,
    }


def review(page, evidence, **details):
    return result(page, evidence, "REVIEW", **details)


def text_of(lines):
    return " ".join(l["text"] for l in lines)


def by_role(page, *roles):
    return [l for l in page["lines"] if l["role"] in roles]


def compact(text):
    return re.sub(r"\s+", "", text).casefold()


def is_author(text):
    """Presence screen, not verification of a person's identity or authorship."""
    if DATE.search(text) or QUESTION.fullmatch(text) or len(text) > 80:
        return False
    if re.search(
        r"^(?:author|presenter|speaker|by|作者|报告人|讲者)\s*[:： ]",
        text,
        re.IGNORECASE,
    ) or re.search(r"示例作者|匿名作者", text):
        return True
    if re.fullmatch(r"[\u4e00-\u9fff]{2,5}", text):
        return True
    # Require a byline-shaped name; institutions, subtitles and prose are not bylines.
    return bool(
        re.fullmatch(
            r"(?:[A-Z][a-zÀ-ÿ]+|[A-Z]\.)(?:[ -](?:[A-Z][a-zÀ-ÿ]+|[A-Z]\.)){1,4}", text
        )
    )


def extract(page, number, total, profile, tex=None):
    cfg = measurement_config()
    g = measure.geometry(page, cfg)
    lines = measure.extract_lines(page, cfg)
    # Geometric cover detection in the reusable extractor is only a bootstrap.
    measure.classify(lines, g, cfg)
    header = g["header"] if g["header"] is not None else 0
    footer = g["footer"] if g["footer"] is not None else page.rect.height
    for l in lines:
        if l["bbox"][3] <= header + 1:
            l["role"] = "navigation"
        elif l["baseline"] >= footer:
            l["role"] = "footer"
        elif number == 1:
            l["role"] = "cover"
        elif l["role"] == "cover":
            l["role"] = "body"
        if QUESTION.fullmatch(l["text"]) and header < l["baseline"] < footer:
            l["role"] = "closing_question"
    candidates = [
        l
        for l in lines
        if l["role"] not in {"navigation", "footer", "closing_question"}
    ]
    if number != 1 and candidates:
        top = min(l["bbox"][1] for l in candidates)
        for l in candidates:
            if l["bbox"][1] < top + 2 and l["bbox"][1] < page.rect.height * 0.25:
                l["role"] = "frame_title"
    # Recover captions for raster figures and vector figures/tables. No caption
    # is identified by a private string or its position in a historical deck.
    objects = g["images"] + g["tables"]
    vector_regions = []
    try:
        vector_regions = [
            list(r)
            for r in page.cluster_drawings()
            if r.width > page.rect.width * 0.12
            and r.height > page.rect.height * 0.08
            and r.y0 > header
            and r.y1 < footer
        ]
    except (AttributeError, ValueError):
        pass
    objects += vector_regions
    bullet_blocks = {l["block"] for l in lines if l["bullet"]}
    for l in candidates:
        if l["block"] in bullet_blocks:
            l["role"] = "body"
            continue
        if l["role"] == "code":
            continue
        prefix = bool(
            re.match(
                r"^(?:Figure|Fig\.|Table|图\s*\d|表\s*\d)", l["text"], re.IGNORECASE
            )
        )
        below = any(
            -0.5 <= l["bbox"][1] - o[3] <= 18
            and o[0] - 3 <= l["bbox"][0]
            and l["bbox"][2] <= o[2] + 3
            for o in objects
        )
        inside = any(
            o[0] - 1 <= l["bbox"][0] and l["bbox"][2] <= o[2] + 1
            and o[1] - 1 <= l["bbox"][1] and l["bbox"][3] <= o[3] + 1
            for o in objects
        )
        prose = len(re.findall(r"[A-Za-z]+", l["text"])) >= 4 or len(re.findall(r"[\u3400-\u9fff]", l["text"])) >= 8
        caption_style = (
            abs(l["size"] - cfg["font_pdf_pt"]["caption"]) <= cfg["limits"]["font_tolerance_pt"]
            if profile == "v19" else l["size"] < cfg["font_pdf_pt"]["body"] * 0.8
        )
        detached = (
            caption_style and prose and not inside
            and l["bbox"][1] > page.rect.height * 0.45
            and bool(re.search(r"[。.!?！？]$", l["text"]))
        )
        if l["role"] == "caption" and inside and not prefix:
            l["role"] = "body"  # plot tick/legend labels are inside the object
        if l["role"] != "frame_title" and (prefix or below and l["size"] < 9 and not inside or detached):
            l["role"] = "caption"
        elif (
            l["role"] == "body"
            and l["spans"]
            and all(
                s["flags"] & 16 or re.search("bold|demi", s["font"], re.IGNORECASE)
                for s in l["spans"]
            )
        ):
            l["role"] = "subhead"
    caption_blocks = {
        (l["block"], round(l["size"], 1)) for l in lines if l["role"] == "caption"
    }
    for l in lines:
        if (l["block"], round(l["size"], 1)) in caption_blocks and l["role"] == "body":
            l["role"] = "caption"
    for l in lines:
        for s in l["spans"]:
            if "math" not in s["font"].lower():
                s["role"] = l["role"]
    raster = measure.raster_stats(page, g, lines, None, cfg)
    try:
        columns = (
            measure.column_measure(lines, g, raster["body_top"], cfg)
            if number != 1
            else None
        )
    except (KeyError, ValueError, ZeroDivisionError):
        columns = None
    grouped = defaultdict(list)
    for l in lines:
        if l["role"] == "caption":
            grouped[l["block"]].append(l)
    captions = [
        {
            "text": text_of(sorted(ls, key=lambda l: l["baseline"])),
            "lines": ls,
            "bbox": measure.union([l["bbox"] for l in ls]),
        }
        for ls in grouped.values()
    ]
    visible = [l for l in lines if l["role"] not in {"navigation", "footer"}]
    p = {
        "number": number,
        "total": total,
        "geometry": g,
        "lines": lines,
        "raster": raster,
        "line_pairs": measure.line_pairs(lines, cfg),
        "columns": columns,
        "captions": captions,
        "objects": objects,
        "profile": profile,
        "tex": tex,
        "text": text_of(visible),
        "all_text": text_of(lines),
        "layout": "cover" if number == 1 else "columns" if columns else "text",
    }
    cover = by_role(p, "cover")
    if cover:
        max_size = max(l["size"] for l in cover)
        p["cover_dates"] = [l for l in cover if DATE.search(l["text"])]
        date_size = max([l["size"] for l in p["cover_dates"]], default=0)
        p["cover_titles"] = [
            l
            for l in cover
            if l["size"] >= max_size * 0.88
            and l["size"] >= date_size * 1.2
            and not DATE.search(l["text"])
        ]
        title_ids = {id(l) for l in p["cover_titles"]}
        p["cover_authors"] = [
            l for l in cover if id(l) not in title_ids and is_author(l["text"])
        ]
        # TeX is optional evidence only if that author also appears in the PDF.
        if tex:
            for author in re.findall(r"\\author(?:\[[^\]]*\])?\s*\{([^{}]+)\}", tex):
                for l in cover:
                    if (
                        compact(author) == compact(l["text"])
                        and id(l) not in title_ids
                        and l not in p["cover_authors"]
                    ):
                        p["cover_authors"].append(l)
    else:
        p.update(cover_titles=[], cover_dates=[], cover_authors=[])
    return p


def check_geometry(p, r, ctx):
    w, h = p["geometry"]["width"], p["geometry"]["height"]
    t = r["thresholds"]
    expected = [t["width"] * 72 / 25.4, t["height"] * 72 / 25.4]
    return (
        [
            result(
                p,
                f"页面尺寸 {w:.2f}×{h:.2f} pt，配置要求 {expected[0]:.2f}×{expected[1]:.2f} pt。",
                actual=[w, h],
                expected=expected,
            )
        ]
        if max(abs(w - expected[0]), abs(h - expected[1])) > t["tolerance_pdf_pt"]
        else []
    )


def check_cover_title(p, r, ctx):
    if p["number"] != 1:
        return []
    return (
        []
        if any(
            len(l["text"].strip()) >= r["thresholds"]["minimum_title_characters"]
            for l in p["cover_titles"]
        )
        else [result(p, "首页没有可识别的可见标题。")]
    )


def check_cover_author(p, r, ctx):
    if p["number"] != 1:
        return []
    return (
        []
        if p["cover_authors"]
        else [
            result(p, "首页没有可识别的可见作者行；题目、日期和研究正文不能代替作者。")
        ]
    )


def check_cover_date(p, r, ctx):
    if p["number"] != 1:
        return []
    return [] if p["cover_dates"] else [result(p, "首页没有可识别的可见日期。")]


def pattern_findings(p, pattern, label, lines=None):
    out = []
    for l in (
        lines
        if lines is not None
        else [l for l in p["lines"] if l["role"] != "navigation"]
    ):
        for match in pattern.finditer(l["text"]):
            out.append(
                result(p, f"{label}：{match.group(0)}", text=l["text"], bbox=l["bbox"])
            )
    return out


def check_audit_tokens(p, r, ctx):
    return pattern_findings(p, AUDIT, "可见审计或执行标记")


def check_file_paths(p, r, ctx):
    out = []
    for l in p["lines"]:
        if l["role"] == "navigation":
            continue
        for match in PATH.finditer(l["text"]):
            token = match[0]
            # A callable attribute with an extension-shaped name is not a
            # filename. This uses syntax, never a library/name whitelist.
            if not re.search(r"[/\\]", token) and re.match(
                r"\s*\(", l["text"][match.end() :]
            ):
                continue
            out.append(
                result(
                    p,
                    f"可见文件路径或内部文件名：{token}",
                    text=l["text"],
                    bbox=l["bbox"],
                )
            )
    return out


def check_internal_versions(p, r, ctx):
    return pattern_findings(p, VERSION, "可见内部版本标记")


def text_blocks(p, include_footer=False):
    groups = defaultdict(list)
    for l in p["lines"]:
        if l["role"] != "navigation" and (include_footer or l["role"] != "footer"):
            groups[l["block"]].append(l)
    return [
        {"text": text_of(ls), "bbox": measure.union([l["bbox"] for l in ls]), "lines": ls}
        for ls in groups.values()
    ]


def configured_patterns(p, r, label):
    t = r["thresholds"]
    pattern = re.compile("|".join(t["patterns"]), re.IGNORECASE)
    allowed = [re.compile(x, re.IGNORECASE) for x in t.get("allow_patterns", [])]
    out = []
    for block in text_blocks(p):
        masked = block["text"]
        for pat in allowed:
            masked = pat.sub(lambda m: " " * len(m[0]), masked)
        for m in pattern.finditer(masked):
            out.append(result(p, f"{label}：{block['text'][m.start():m.end()]}",
                              text=block["text"], bbox=block["bbox"]))
    return out


def check_contrast(p, r, ctx):
    return configured_patterns(p, r, "模板化对比句式")


def check_meta(p, r, ctx):
    return configured_patterns(p, r, "可见元说明或内部执行标签")


def check_word_budget(p, r, ctx):
    text = p["text"]
    han = len(re.findall(r"[\u3400-\u9fff]", text))
    units = len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text)) + han / 2
    return (
        [
            result(
                p,
                f"本页文字量 {units:g} 单位，超过配置上限 {r['thresholds']['max_units']}。",
                units=units,
            )
        ]
        if units > r["thresholds"]["max_units"]
        else []
    )


def check_extractability(p, r, ctx):
    return (
        []
        if len(p["text"].strip()) >= r["thresholds"]["min_visible_characters"]
        else [result(p, "无可提取的可见正文；文字检测未覆盖此页，须 OCR 或人工检查。")]
    )


def caption_patterns(p, pattern, label):
    return [
        result(p, f"{label}：{m.group(0)}", text=c["text"], bbox=c["bbox"])
        for c in p["captions"]
        for m in pattern.finditer(c["text"])
    ]


def check_caption_joiners(p, r, ctx):
    return caption_patterns(p, re.compile(r"[·;；]"), "图注含串联分隔符")


def check_caption_runtime(p, r, ctx):
    return caption_patterns(p, RUNTIME, "图注含耗时陈述")


def check_caption_version(p, r, ctx):
    return caption_patterns(p, DATA_VERSION, "图注含数据版本或来源核算")


def check_caption_sentences(p, r, ctx):
    out = []
    for c in p["captions"]:
        text = re.sub(
            r"\b(?:Fig|Eq|et al)\.", lambda m: m[0].replace(".", ""), c["text"]
        )
        text = re.sub(r"(?<=\d)\.(?=\d)", "", text)
        sentences = [s for s in re.split(r"[。！？!?]+|\.(?:\s+|$)", text) if s.strip()]
        if len(sentences) > r["thresholds"]["max_sentences"]:
            out.append(
                result(
                    p,
                    f"图注包含 {len(sentences)} 句，要求一句。",
                    text=c["text"],
                    bbox=c["bbox"],
                )
            )
    return out


def check_question_style(p, r, ctx):
    out = []
    t = r["thresholds"]
    w = p["geometry"]["width"]
    for l in by_role(p, "closing_question"):
        dx = abs((l["bbox"][0] + l["bbox"][2]) / 2 - w / 2) * 1920 / w
        if (
            abs(l["size"] - t["font_pdf_pt"]) > t["tolerance_pdf_pt"]
            or dx > t["horizontal_error_max_px"]
        ):
            out.append(
                result(
                    p,
                    f"问题块字号 {l['size']:.3f} pt，水平偏差 {dx:.2f} px。",
                    size=l["size"],
                    horizontal_px=dx,
                )
            )
    return out


def body_track(p):
    h = p["geometry"]["height"]
    return (
        (46 * h / 255.12, 245 * h / 255.12)
        if p["profile"] == "v19"
        else (h * 0.18, p["geometry"]["footer"] or h * 0.95)
    )


def check_question_y(p, r, ctx):
    out = []
    top, bottom = body_track(p)
    t = r["thresholds"]
    for l in by_role(p, "closing_question"):
        y = ((l["bbox"][1] + l["bbox"][3]) / 2 - top) / (bottom - top)
        if abs(y - t["center_target"]) > t["tolerance"] + 1e-7:
            out.append(
                result(
                    p,
                    f"问题块中心为正文轨道的 {y:.1%}，要求 {t['center_target']:.0%}±{t['tolerance']:.0%}。",
                    fraction=y,
                )
            )
    return out


def screen_cover(p, r, ctx):
    if p["number"] != 1:
        return []
    allowed = {
        id(l)
        for key in ["cover_titles", "cover_authors", "cover_dates"]
        for l in p[key]
    }
    extras = [l for l in p["lines"] if l["role"] not in {"navigation", "footer"} and id(l) not in allowed]
    return (
        [
            result(
                p,
                "首页含标题、作者、日期之外的文字或图表。",
                text=text_of(extras), objects=p["objects"],
            )
        ]
        if extras or p["objects"]
        else []
    )


def check_closing_question(p, r, ctx):
    if p["number"] not in ctx["closing_pages"]:
        return []
    if by_role(p, "closing_question"):
        return []
    return [result(p, "末页缺少可见 Questions? 问题块。",
                   boundary=ctx["closing_pages"][p["number"]])]


def screen_closing(p, r, ctx):
    qs = by_role(p, "closing_question")
    out = []
    if r["id"] == "ROLE-CLOSING-CONTENT":
        if qs and not any(
            l["role"] in {"body", "short_label", "subhead"}
            and l["bbox"][3] < qs[0]["bbox"][1]
            for l in p["lines"]
        ):
            out.append(review(p, "问题块上方没有可识别的结论或要点。"))
        if p["number"] == p["total"] and not ctx["has_question"]:
            out.append(review(p, "整套未识别到问题块；确认结尾是否含要点及讨论。"))
    else:
        if qs or p["number"] == p["total"]:
            for l in p["lines"]:
                if l["role"] in {"navigation", "footer"}:
                    continue
                if re.search(
                    r"@|https?://|\b(?:email|contact|QR|LMS)\b|联系|二维码",
                    l["text"],
                    re.IGNORECASE,
                ):
                    out.append(
                        review(p, "结尾出现联系方式或资源链接。", text=l["text"])
                    )
    return out


def screen_prose(p, r, ctx):
    ident = r["id"]
    out = []
    if ident == "TEXT-NO-META":
        pat = re.compile(
            r"本页|本次汇报|已经(?:完成|检查)|\b(?:we checked|verified|audited|contract|implementation status|evidence status)\b",
            re.IGNORECASE,
        )
    elif ident == "TEXT-NO-ENDING-DISCLAIMER":
        pat = re.compile(
            r"\b(?:does not mean|does not imply|remains pending|for reference only|not financial advice)\b|仅供参考|不代表|不意味着|尚待确认|最终解释权",
            re.IGNORECASE,
        )
    else:
        pat = re.compile(
            r"赋能|闭环|全面提升|携手|共创|\b(?:unlock the power|game[- ]changing|revolutionary|key takeaway:)\b",
            re.IGNORECASE,
        )
    for f in pattern_findings(p, pat, "需判断的套话、过程用语或免责陈述"):
        out.append({**f, "status": "REVIEW"})
    if ident == "TEXT-NO-LABEL-PHRASES":
        for line in p["lines"]:
            if line["role"] not in {"body", "short_label", "subhead", "table", "caption"}:
                continue
            words = re.findall(r"[A-Za-z]+", line["text"])
            han = re.findall(r"[\u3400-\u9fff]", line["text"])
            if (1 <= len(words) <= 14 or 1 <= len(han) <= 28) and not re.search(r"[.!?。！？]$", line["text"]):
                out.append(review(p, "检查标签式短语是否缺少对象、关系或解释。",
                                  text=line["text"], bbox=line["bbox"]))
    elif ident == "TEXT-NO-ENDING-DISCLAIMER":
        blocks = [b for b in text_blocks(p) if any(l["role"] not in {"frame_title", "closing_question"} for l in b["lines"])]
        if blocks:
            last = max(blocks, key=lambda b: b["bbox"][3])
            out.append(review(p, "核对本页末句是否增加信息，或仅重复标题、作空泛免责。",
                              text=last["text"], bbox=last["bbox"]))
    return out


def screen_abbreviations(p, r, ctx):
    caption_only = r["id"] == "CAP-NO-UNDEFINED-TERMS"
    out = []
    for term, first in ctx["first_abbreviation"].items():
        if first["page"] != p["number"] or first["defined"]:
            continue
        if caption_only and first["role"] != "caption":
            continue
        hit = result if r["id"] == "TEXT-UNDEFINED-ABBREVIATIONS" else review
        out.append(hit(p, f"缩写 {term} 首次出现处或之前未找到展开定义。",
                       term=term, text=first["text"], bbox=first["bbox"],
                       definition_policy="Explicit expansion at or before first occurrence; later definitions do not repair it."))
    return out


def screen_captions(p, r, ctx):
    out = []
    ident = r["id"]
    tol = 2 * p["geometry"]["width"] / 1920
    if ident == "CAP-REQUIRED":
        for o in p["objects"]:
            if not any(0 <= c["bbox"][1] - o[3] <= 20 for c in p["captions"]):
                outside = [
                    l for l in p["lines"]
                    if l["role"] in {"body", "subhead"}
                    and measure.intersection(l["bbox"], o) <= 0
                    and (len(re.findall(r"[A-Za-z]+", l["text"])) >= 5
                         or len(re.findall(r"[\u3400-\u9fff]", l["text"])) >= 10)
                ]
                if not outside and not p["captions"]:
                    out.append(result(p, "图表既无关联图注，也无可识别的正文解释。", bbox=o))
                else:
                    out.append(review(p, "图表未配关联图注；核对外部正文是否充分解释。",
                                      bbox=o, candidates=[l["text"] for l in outside]))
    for c in p["captions"]:
        below = [o for o in p["objects"] if -0.5 <= c["bbox"][1] - o[3] <= 20]
        if ident == "CAP-BELOW-OBJECT" and not below:
            out.append(review(p, "图注上方未找到可关联的本页对象。", text=c["text"]))
        if ident in {"CAP-LINE-AWARE-ALIGNMENT", "CAP-MULTILINE-ANCHOR"} and below:
            obj = min(below, key=lambda o: abs(c["bbox"][1] - o[3]))
            ls = c["lines"]
            error = (
                abs((c["bbox"][0] + c["bbox"][2] - obj[0] - obj[2]) / 2)
                if len(ls) == 1
                else max(abs(l["bbox"][0] - obj[0]) for l in ls)
            )
            if error > tol:
                out.append(
                    review(
                        p,
                        f"图注按实际 {len(ls)} 行计算的对齐偏差为 {error * 1920 / p['geometry']['width']:.2f} px。",
                        bbox=c["bbox"],
                    )
                )
        if ident == "CAP-NO-BARE-RESULTS" and re.search(
            r"(?:^|[:：=;；·])\s*(?:\w+\s*[=:]\s*)?[-+]?\d+(?:\.\d+)?%?\s*(?:$|[;；·])",
            c["text"],
        ):
            out.append(review(p, "图注含独立数字结果片段。", text=c["text"]))
        if ident == "CAP-NATURAL-SENTENCE":
            out.append(
                review(p, "检查这句是否说明图表展示什么、比较什么，或只是元判断。", text=c["text"])
            )
    return out


def screen_typography(p, r, ctx):
    ident = r["id"]
    out = []
    t = r["thresholds"]
    w = p["geometry"]["width"]
    role = {
        "TYPE-COVER-TITLE": "cover",
        "TYPE-COVER-BYLINE": "cover",
        "TYPE-FRAME-TITLE": "frame_title",
        "TYPE-BODY": "body",
        "TYPE-SUBHEAD": "subhead",
        "TYPE-TABLE": "table",
        "TYPE-CODE": "code",
        "TYPE-CAPTION": "caption",
        "TYPE-FOOTER": "footer",
        "TYPE-NAVIGATION": "navigation",
    }.get(ident)
    if role:
        ls = (
            p["cover_titles"]
            if ident == "TYPE-COVER-TITLE"
            else p["cover_authors"] + p["cover_dates"]
            if ident == "TYPE-COVER-BYLINE"
            else by_role(p, role)
        )
        target = t.get("font_pdf_pt", t.get("font_tex_pt", 0) * 72 / 72.27)
        for l in ls:
            spans = [
                s
                for s in l["spans"]
                if "math" not in s["font"].lower() and not s["flags"] & 1
            ]
            if any(
                abs(s["size"] - target)
                > t.get("tolerance_pdf_pt", t.get("font_tolerance_pdf_pt", 0.1))
                for s in spans
            ):
                out.append(
                    review(
                        p,
                        f"{role} 候选字号 {l['size']:.3f} pt，配置为 {target:.3f} pt；确认角色。",
                        text=l["text"],
                        bbox=l["bbox"],
                    )
                )
            if t.get("weight") == "bold" and not any(
                s["flags"] & 16 or re.search("bold|demi", s["font"], re.IGNORECASE)
                for s in spans
            ):
                out.append(review(p, "候选文字未识别为规定粗体。", text=l["text"]))
            if (
                t.get("alignment") == "center"
                and abs((l["bbox"][0] + l["bbox"][2]) / 2 - w / 2) > 2 * w / 1920
            ):
                out.append(review(p, "封面文字未在水平中心。", text=l["text"]))
    if ident == "TYPE-DECK-CONSISTENCY":
        for l in by_role(p, "body"):
            typical = ctx["role_sizes"].get("body")
            if typical and l["size"] < typical * 0.9:
                out.append(
                    review(
                        p,
                        "正文候选字号小于全套正文常用字号，确认是否局部缩字。",
                        size=l["size"],
                        typical=typical,
                        text=l["text"],
                    )
                )
    if ident == "TYPE-NORMAL-LEADING":
        target = t["body_baseline_tex_pt"] * 72 / 72.27
        for pair in p["line_pairs"]:
            if (
                pair["role"] == "body"
                and not pair["bullet"]
                and pair["delta_pt"] < target - 0.5
            ):
                out.append(
                    review(
                        p,
                        f"候选正文行距 {pair['delta_pt']:.2f} pt 小于正常值 {target:.2f} pt。",
                        bbox=measure.union([pair["a"], pair["b"]]),
                    )
                )
    if ident == "TYPE-FONT-FAMILIES":
        families = "texgyretermes|newcm|newcomputermodern|notoserif|notosans|lmmono|latinmodernmono|lmsans|cmsy|cmex"
        for l in p["lines"]:
            for s in l["spans"]:
                if not re.search(families, s["font"], re.IGNORECASE):
                    out.append(
                        review(
                            p,
                            "字体家族不在模板声明列表内；文件绑定仍需源码确认。",
                            font=s["font"],
                            text=s["text"],
                        )
                    )
    if ident == "TYPE-LIST-STYLE":
        markers = set()
        for l in p["lines"]:
            m = re.match(r"^(•|‣|–|\d+[.)])\s*", l["text"])
            if m:
                markers.add("numbered" if m[1][0].isdigit() else m[1])
        if len(markers) > 1:
            out.append(
                review(
                    p,
                    "本页混用列表标记，确认是否属于同一层级。",
                    markers=sorted(markers),
                )
            )
    return out


def screen_tex(p, r, ctx):
    # The PDF remains the primary artifact. Missing/unsupported TeX is REVIEW.
    if p["number"] != 1:
        return []
    if not p["tex"]:
        return [review(p, "未提供 TeX；源码级规则需要人工或其他工具的原生源文件。")]
    tex = re.sub(r"(?<!\\)%[^\n]*", "", p["tex"])
    out = []
    patterns = {
        "TYPE-NO-COMPRESSION": [
            r"\\vspace\*?\s*\{\s*-\s*\d",
            r"\\nointerlineskip",
            r"\\(?:renewcommand|def)\s*\{?\\arraystretch\}?\s*\{\s*0(?:\.\d+)?\s*\}",
            r"\\setlength\s*\{\\tabcolsep\}\s*\{\s*[012](?:\.\d+)?\s*pt\s*\}",
        ],
        "TYPE-LIST-PARAMETERS": [
            r"\\setlength\s*\{\\(?:itemsep|topsep|parsep|parskip)\}\s*\{[^}]*\}"
        ],
        "ROLE-QUESTION-PRIMITIVE": [r"\\begin\{(?:tcolorbox|mdframed)\}"],
    }
    for pattern in patterns.get(r["id"], []):
        for m in re.finditer(pattern, tex):
            out.append(
                review(
                    p,
                    "源码含需核对的局部排版覆盖。",
                    source_line=tex[: m.start()].count("\n") + 1,
                    command=m[0],
                )
            )
    return out


def screen_overflow(p, r, ctx):
    out = []
    g = p["geometry"]
    w, h = g["width"], g["height"]
    tol = 2 * w / 1920
    groups = {
        "text": [l["bbox"] for l in p["lines"]],
        "image": g["images"],
        "vector": g["vectors"],
    }
    for kind, rects in groups.items():
        for b in rects:
            if b[0] < -tol or b[1] < -tol or b[2] > w + tol or b[3] > h + tol:
                out.append(
                    review(
                        p,
                        "对象范围越出物理页；确认最终裁剪后是否仍有可见越界。",
                        kind=kind,
                        bbox=b,
                    )
                )
    return out


def screen_footer(p, r, ctx):
    ident = r["id"]
    g = p["geometry"]
    out = []
    ls = by_role(p, "footer")
    w = g["width"]
    if ident == "FOOT-NECESSARY-SOURCES":
        for l in ls:
            if l["bbox"][0] < w / 2 and not SOURCE.search(l["text"]):
                out.append(
                    review(
                        p,
                        "左页脚不是可识别的来源说明，确认是否应删除。",
                        text=l["text"],
                    )
                )
    if ident == "FOOT-NATIVE-COMPONENTS":
        counters = [l for l in ls if re.search(r"\b\d+\s*/\s*\d+\b", l["text"])]
        if g["footer"] is None:
            out.append(review(p, "未识别到全宽页脚分隔线。"))
        if not counters:
            out.append(review(p, "未识别到 current/total 页码。"))
        if not g["footer_controls"]:
            out.append(review(p, "未识别到原生页脚控件。"))
    if ident in {"FOOT-OPTICAL-CENTERS", "FOOT-SOURCE-REFINEMENT"}:
        centers = p["raster"]["footer_center_offsets_px"]
        t = r["thresholds"]
        for key, val in centers.items():
            limit = t.get("center_error_max", t.get("source_to_band_max"))
            if ident == "FOOT-SOURCE-REFINEMENT" and key != "left":
                continue
            if abs(val) > limit:
                out.append(
                    review(
                        p,
                        f"页脚 {key} 墨迹中心偏差 {val:.2f} px，门槛 {limit} px。",
                        offset_px=val,
                    )
                )
        peer_limit = t.get("peer_center_spread_max", t.get("source_to_counter_max"))
        vals = (
            list(centers.values())
            if ident == "FOOT-OPTICAL-CENTERS"
            else [centers[k] for k in ["left", "counter"] if k in centers]
        )
        if len(vals) > 1 and max(vals) - min(vals) > peer_limit:
            out.append(
                review(p, "页脚组之间的墨迹中心差超过配置值。", centers_px=centers)
            )
    if ident == "FOOT-SAFE-ZONE" and ls:
        body = by_role(p, "body", "caption", "code", "table")
        bottom = max([l["bbox"][3] for l in body], default=0)
        gap = min(l["bbox"][1] for l in ls) - bottom
        out.append(
            review(
                p,
                f"正文至页脚文字框间距 {gap:.2f} pt；通用最小安全距离尚未冻结。",
                gap_pt=gap,
            )
        )
    return out


def screen_spacing(p, r, ctx):
    if p["number"] == 1:
        return []
    # Candidate relations are reported with actual roles; unknown semantic
    # relations remain in the per-page checklist, never silently accepted.
    blocks = defaultdict(list)
    for l in p["lines"]:
        if l["role"] not in {"navigation", "footer", "frame_title"}:
            blocks[(l["block"], l["role"])].append(l)
    units = []
    for group in blocks.values():
        current = []
        for l in sorted(group, key=lambda l: l["baseline"]):
            if l["bullet"] and current:
                units.append(current)
                current = []
            current.append(l)
        if current:
            units.append(current)
    ls = sorted(
        [
            {
                **unit[0],
                "bbox": measure.union([l["bbox"] for l in unit]),
                "text": text_of(unit),
            }
            for unit in units
        ],
        key=lambda l: l["bbox"][1],
    )
    t = r["thresholds"]
    band = t.get("target", t.get("B_projection"))
    out = []
    relations = {
        "LIST-ITEM-GAP": lambda a, b: a["bullet"] and b["bullet"],
        "PARAGRAPH-TO-LIST": lambda a, b: (
            a["role"] == "body" and not a["bullet"] and b["bullet"]
        ),
        "PARAGRAPH-TO-DISPLAY-MATH": lambda a, b: (
            a["role"] == "body" and b["role"] == "math"
        ),
        "DISPLAY-MATH-TO-BODY": lambda a, b: (
            a["role"] == "math" and b["role"] == "body"
        ),
        "CAPTION-TO-BODY": lambda a, b: a["role"] == "caption" and b["role"] == "body",
        "QUESTION-TO-NEXT": lambda a, b: a["role"] == "closing_question",
        "WITHIN-GROUP": lambda a, b: (
            a["block"] == b["block"] and a["role"] == b["role"]
        ),
        "BETWEEN-GROUP": lambda a, b: a["block"] != b["block"],
    }
    suffix = r["id"].removeprefix("LAY-SPACE-")
    for a, b in pairwise(ls):
        if min(a["bbox"][2], b["bbox"][2]) <= max(a["bbox"][0], b["bbox"][0]):
            continue
        predicate = relations.get(suffix)
        if not predicate or not predicate(a, b):
            continue
        gap = b["bbox"][1] - a["bbox"][3]
        if band and not band[0] <= gap <= band[1]:
            out.append(
                review(
                    p,
                    f"候选 {suffix.lower()} 可见文字框间距 {gap:.2f} pt，目标 {band}；须核对完整墨迹边界及语义配对。",
                    gap_pdf_box_pt=gap,
                    bboxes=[a["bbox"], b["bbox"]],
                )
            )
    # Object-pair relations include raster and vector chart/table regions.
    object_kinds = {
        "PARAGRAPH-TO-TABLE": "body",
        "PARAGRAPH-TO-FIGURE": "body",
        "DISPLAY-MATH-TO-TABLE": "math",
        "TABLE-TO-INTERPRETATION": "body",
    }
    if suffix in object_kinds:
        objs = p["geometry"]["tables"] if "TABLE" in suffix else p["objects"]
        for o in objs:
            candidates = [
                l
                for l in ls
                if l["role"] == object_kinds[suffix]
                and (
                    l["bbox"][1] >= o[3]
                    if suffix == "TABLE-TO-INTERPRETATION"
                    else l["bbox"][3] <= o[1]
                )
            ]
            if not candidates:
                continue
            l = min(
                candidates,
                key=lambda l: (
                    abs(l["bbox"][1] - o[3])
                    if suffix == "TABLE-TO-INTERPRETATION"
                    else abs(o[1] - l["bbox"][3])
                ),
            )
            gap = (
                l["bbox"][1] - o[3]
                if suffix == "TABLE-TO-INTERPRETATION"
                else o[1] - l["bbox"][3]
            )
            if band and not band[0] <= gap <= band[1]:
                out.append(
                    review(
                        p,
                        f"候选对象间距 {gap:.2f} pt 超出目标 {band}。",
                        bboxes=[o, l["bbox"]],
                    )
                )
    if suffix in {"MAJOR-SECTION", "TITLE-TO-QUESTION"}:
        titles = by_role(p, "frame_title")
        target = (
            next((l for l in ls if l["role"] == "closing_question"), None)
            if suffix == "TITLE-TO-QUESTION"
            else next(iter(ls), None)
        )
        if titles and target:
            gap = target["bbox"][1] - max(l["bbox"][3] for l in titles)
            if band and not band[0] <= gap <= band[1]:
                out.append(
                    review(
                        p,
                        f"标题至候选内容间距 {gap:.2f} pt，需核对适用角色。",
                        gap_pt=gap,
                    )
                )
    return out


def screen_layout(p, r, ctx):
    ident = r["id"]
    g = p["geometry"]
    w, h = g["width"], g["height"]
    out = []
    t = r["thresholds"]
    body = by_role(
        p, "body", "math", "caption", "code", "table", "short_label", "closing_question"
    )
    if ident == "LAY-RAILS" and p["number"] != 1:
        rail = t["left"] * 72 / 25.4
        for l in body:
            if l["bbox"][0] < rail - 0.5 or l["bbox"][2] > w - rail + 0.5:
                out.append(
                    review(
                        p,
                        "正文候选对象超出配置左右留白。",
                        bbox=l["bbox"],
                        rail_pt=rail,
                    )
                )
    elif (
        ident == "LAY-BODY-WHITESPACE"
        and p["number"] != 1
        and not by_role(p, "closing_question")
    ):
        top, bottom = body_track(p)
        # Raster edges exclude invisible PDF paths and wholly empty containers.
        pix = ctx["page"].get_pixmap(
            matrix=pdf.Matrix(960 / w, 540 / h), alpha=False, colorspace=pdf.csRGB
        )
        rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
            pix.height, pix.width, 3
        )
        ink = np.min(rgb, axis=2) < 220
        crop = ink[
            round(top * 540 / h) : round(bottom * 540 / h),
            round(w * 0.05 * 960 / w) : round(w * 0.95 * 960 / w),
        ]
        rows = np.where(crop.any(axis=1))[0]
        if len(rows):
            fractions = [
                (rows[-1] - rows[0]) / len(crop),
                rows[0] / len(crop),
                (len(crop) - 1 - rows[-1]) / len(crop),
            ]
        else:
            fractions = [0, 1, 1]
        if (
            fractions[0] < t["span_min"]
            or fractions[1] > t["top_blank_max"]
            or fractions[2] > t["bottom_blank_max"]
        ):
            # Only an explicitly selected template supplies a frozen body
            # track. Generic pages retain REVIEW for unknown template intent.
            hit = result if p["profile"] == "v19" else review
            out.append(
                hit(
                    p,
                    f"正文纵向跨度 {fractions[0]:.1%}，上/下留白 {fractions[1]:.1%}/{fractions[2]:.1%}；要求跨度 ≥{t['span_min']:.0%}，外留白各 ≤{t['top_blank_max']:.0%}/{t['bottom_blank_max']:.0%}。",
                    fractions=fractions, track_pdf_pt=[top, bottom],
                    thresholds={k: t[k] for k in ["span_min", "top_blank_max", "bottom_blank_max"]},
                )
            )
    elif (
        ident
        in {
            "LAY-COLUMN-PRESETS",
            "LAY-COLUMN-ANCHORS",
            "LAY-COLUMN-BOTTOMS",
            "LAY-COLUMN-REASON",
            "ROLE-FULL-WIDTH-TRANSITION",
        }
        and p["columns"]
    ):
        c = p["columns"]
        if ident == "LAY-COLUMN-BOTTOMS" and c["bottom_delta_px"] > 100:
            out.append(
                review(
                    p,
                    f"并列栏底部差 {c['bottom_delta_px']:.1f} px，超过 100 px 复核线。",
                    columns=c,
                )
            )
        elif ident == "LAY-COLUMN-PRESETS":
            out.append(
                review(
                    p,
                    "检测到双栏；按声明的容器宽度、3–4% 沟槽核对，墨迹宽度不能代替容器宽度。",
                    columns=c,
                )
            )
        elif ident == "LAY-COLUMN-ANCHORS":
            rects = c.get("left"), c.get("right")
            if all(rects):
                delta = abs(rects[0][1] - rects[1][1]) * 1080 / h
                if delta > 2:
                    out.append(
                        review(
                            p,
                            f"候选双栏顶部差 {delta:.2f} px；确认声明的 top/baseline 锚点。",
                            columns=c,
                        )
                    )
        elif ident == "ROLE-FULL-WIDTH-TRANSITION" and c.get("full_width_below"):
            out.append(
                review(p, "双栏后检测到通栏内容，确认过渡角色和间距。", columns=c)
            )
        elif ident == "LAY-COLUMN-REASON":
            out.append(review(p, "双栏须确认是并列比较，且阅读顺序明确。", columns=c))
    elif ident == "LAY-CLOSING-ZONES" and by_role(p, "closing_question"):
        top, bottom = body_track(p)
        cut = top + t["upper"] * (bottom - top)
        for l in body:
            if l["role"] != "closing_question" and l["bbox"][3] > cut:
                out.append(
                    review(
                        p, "结尾上半部要点越过声明分区。", bbox=l["bbox"], split_y=cut
                    )
                )
    elif ident == "LAY-COVER-SPACING" and p["number"] == 1:
        out.append(
            review(
                p,
                "已提取封面文字框；lead、byline、date 胶水需与源码和共享模板核对。",
                boxes=[l["bbox"] for l in by_role(p, "cover")],
            )
        )
    elif ident == "LAY-CONTINUATION-ANCHOR":
        for a, b in pairwise(body):
            if a["bullet"] and not b["bullet"] and a["block"] == b["block"]:
                anchor = (
                    a["spans"][1]["bbox"][0]
                    if len(a["spans"]) > 1
                    else a["bbox"][0] + a["size"]
                )
                delta = abs(b["bbox"][0] - anchor) * 1920 / w
                if delta > 2:
                    out.append(
                        review(
                            p,
                            f"列表续行候选锚点偏差 {delta:.2f} px，确认文字而非符号锚点。",
                            bboxes=[a["bbox"], b["bbox"]],
                        )
                    )
    elif ident == "LAY-TABLE-ATOMS":
        for l in by_role(p, "table"):
            if re.search(r"\b\w+-$", l["text"]):
                out.append(
                    review(
                        p,
                        "表格候选文本尾部断词，确认是否拆开语义单位。",
                        text=l["text"],
                    )
                )
    elif ident == "LAY-NAVIGATION-BUDGET":
        for l in by_role(p, "navigation"):
            width = l["bbox"][2] - l["bbox"][0]
            if width > t["absolute_cap"] * w / 453.54:
                out.append(
                    review(
                        p,
                        "导航标签超过配置绝对宽度；精确节数预算需源码。",
                        width_pt=width,
                        text=l["text"],
                    )
                )
    elif ident == "LAY-NAVIGATION-GAPS":
        nav = sorted(by_role(p, "navigation"), key=lambda l: l["bbox"][0])
        for a, b in pairwise(nav):
            gap = (b["bbox"][0] - a["bbox"][2]) * 1920 / w
            if gap < t["neighbor_gap_min"]:
                out.append(
                    review(
                        p,
                        f"相邻导航标签候选间距 {gap:.2f} px。",
                        text=a["text"] + " / " + b["text"],
                    )
                )
    elif ident.startswith("LAY-DIAGRAM-"):
        out.extend(screen_diagram(p, r, ctx))
    elif ident == "LAY-SPACING-ROLES":
        if len(body) > 1:
            out.append(
                review(
                    p,
                    "已识别相邻文字块；需要声明其语义间距角色，不能用原始 vspace 代替。",
                    blocks=len({l["block"] for l in body}),
                )
            )
    elif ident == "ROLE-EXACTLY-ONE":
        uncertain = by_role(p, "math", "short_label")
        if uncertain:
            out.append(
                review(p, "存在待确认的数学或短标签文字角色。", count=len(uncertain))
            )
    elif ident == "LAY-FIGURE-INTERNAL-READABILITY" and p["objects"]:
        out.append(
            review(
                p,
                "已检测图表；轴、刻度、图例及图内文字需按投影大小确认。",
                objects=p["objects"],
            )
        )
    elif ident == "LAY-SPARSE-RECOMPOSITION" and len(body) < 4 and p["number"] != 1:
        out.append(
            review(
                p,
                "内容较少，确认是否已用固定字号重排而非拉大内部间距。",
                body_lines=len(body),
            )
        )
    return out


def screen_diagram(p, r, ctx):
    ident = r["id"]
    out = []
    w = p["geometry"]["width"]
    tol = 2 * w / 1920
    # Stroke segments are candidates only: axes and mathematical mappings are
    # deliberately not promoted to semantic arrows.
    segments = []
    for d in ctx["page"].get_drawings():
        if not d["color"] or d.get("stroke_opacity", 1) <= 0:
            continue
        for item in d["items"]:
            if item[0] != "l":
                continue
            a, b = item[1:]
            length = abs(b - a)
            if length < 1 or min(a.y, b.y) < p["geometry"]["height"] * 0.1:
                continue
            if abs(a.y - b.y) < 0.01 and length > w * 0.9:
                continue
            segments.append((a, b, length, d["width"]))
    if ident == "LAY-DIAGRAM-SHAFT":
        for a, b, length, _ in segments:
            mm = length * 25.4 / 72
            if mm < 8:
                out.append(
                    review(
                        p,
                        f"候选线段长 {mm:.2f} mm；先确认是否为语义箭杆，再应用 6/8 mm 门槛。",
                        endpoints=[list(a), list(b)],
                    )
                )
    elif ident == "LAY-DIAGRAM-BOUNDARIES":
        for a, b, _, _ in segments:
            for l in by_role(p, "body", "short_label"):
                rect = pdf.Rect(l["bbox"])
                if rect.intersects(
                    pdf.Rect(
                        min(a.x, b.x),
                        min(a.y, b.y),
                        max(a.x, b.x) + tol,
                        max(a.y, b.y) + tol,
                    )
                ):
                    out.append(
                        review(
                            p,
                            "线段候选与文字框相交；确认是否真实穿字或数学标记。",
                            text=l["text"],
                            endpoints=[list(a), list(b)],
                        )
                    )
    elif ident == "LAY-DIAGRAM-PEER-EDGES" and len(segments) > 1:
        out.append(
            review(
                p,
                "检测到多条线段；须确认同组语义边后比较长度与间距。",
                lengths_pt=[s[2] for s in segments],
            )
        )
    elif ident == "LAY-DIAGRAM-SHARED-STYLES" and segments:
        widths = sorted({round(s[3], 3) for s in segments})
        out.append(
            review(
                p,
                "已提取线宽；共享节点、箭头及文本样式仍需源码确认。",
                stroke_widths_pt=widths,
            )
        )
    elif ident == "LAY-DIAGRAM-PADDING":
        for box in p["geometry"].get("panels", []):
            for l in by_role(p, "body", "short_label"):
                b = l["bbox"]
                if (
                    box[0] <= b[0] <= b[2] <= box[2]
                    and box[1] <= b[1] <= b[3] <= box[3]
                ):
                    pad = min(
                        b[0] - box[0], box[2] - b[2], b[1] - box[1], box[3] - b[3]
                    )
                    if pad < 3 * 72 / 72.27:
                        out.append(
                            review(
                                p,
                                f"节点候选最小文字框内边距 {pad:.2f} pt。",
                                text=l["text"],
                            )
                        )
    return out


def expansion_matches(term, expansion):
    words = re.findall(r"[A-Za-z]+", expansion)
    key = re.sub(r"[^A-Za-z]", "", term).upper()
    initials = "".join(w[0] for w in words).upper()
    # Match a suffix so introductory prose before an expansion is harmless.
    stop = {"a", "an", "the", "of", "and", "for", "in", "on", "with"}
    significant = "".join(w[0] for w in words if w.lower() not in stop).upper()
    return len(words) >= 2 and (initials.endswith(key) or significant.endswith(key))


def abbreviation_defined(term, before, tail):
    # Expansion (ABC), ABC (expansion), ABC: expansion, ABC is/means expansion.
    left = re.search(r"([^.!?;:()（）]{3,160})(?:[（(]|[:：])\s*$", before)
    if left and (expansion_matches(term, left[1]) or re.search(r"[\u3400-\u9fff]{2,}", left[1])):
        return True
    right = re.match(r"\s*(?:[（(]([^()（）]+)[)）]|[:：]\s*([^.!?;]+)|(?:is|means|stands for)\s+(?:the\s+)?([^.!?;]+))", tail, re.IGNORECASE)
    if right:
        expansion = next(x for x in right.groups() if x is not None)
        return bool(expansion_matches(term, expansion) or re.search(r"[\u3400-\u9fff]{2,}", expansion))
    # A fully written expansion before the term also counts when colon syntax
    # places the long name first. Arbitrary parentheses do not define a term.
    return False


def build_context(pages, rows=None, outline=None):
    rows = rows or rules()
    config = next(r["thresholds"] for r in rows if r["id"] == "TEXT-UNDEFINED-ABBREVIATIONS")
    whitelist = set(config["whitelist"])
    first = {}
    prior = ""
    role_sizes = defaultdict(list)
    for p in pages:
        visible = [l for l in p["lines"] if l["role"] not in {"navigation", "footer", "code"}]
        page_text = text_of(visible)
        offset = 0
        for l in visible:
            for m in ABBR.finditer(l["text"]):
                term = m[0]
                if re.fullmatch(r"[A-Z]{2,}s", term):
                    term = term[:-1]  # ordinary acronym plural, e.g. ABCs -> ABC
                if term in first or term in whitelist or re.fullmatch(r"[A-Z]\d+", term):
                    continue
                before = (prior + " " + page_text[:offset + m.start()])[-400:]
                tail = page_text[offset + m.end():offset + m.end() + 180]
                defined = abbreviation_defined(term, before, tail)
                first[term] = {"page": p["number"], "defined": defined, "text": l["text"],
                               "bbox": l["bbox"], "role": l["role"]}
            offset += len(l["text"]) + 1
            role_sizes[l["role"]].append(l["size"])
        prior = (prior + " " + page_text)[-1000:]
    closing = {p["total"]: "deck_end" for p in pages}
    appendix = re.compile(r"^(?:appendi(?:x|ces)|backup|supplement(?:ary)?|附录|备用)(?:\b|[:：])", re.IGNORECASE)
    starts = [row[2] for row in (outline or []) if appendix.search(row[1]) and row[2] > 1]
    starts += [p["number"] for p in pages if p["number"] > 1
               and any(appendix.search(l["text"]) for l in by_role(p, "frame_title"))]
    if starts:
        closing[min(starts) - 1] = "main_before_appendix"
    return {
        "first_abbreviation": first,
        "role_sizes": {k: statistics.median(v) for k, v in role_sizes.items()},
        "has_question": any(by_role(p, "closing_question") for p in pages),
        "closing_pages": closing,
    }


def applicable(r, p, profile):
    if r["profile"] == "v19" and profile != "v19":
        return False
    ident = r["id"]
    if "COVER-" in ident:
        return p["number"] == 1
    if ident == "TEXT-CLOSING-QUESTION":
        return True
    if ident.startswith("CAP-") or ident == "TYPE-CAPTION":
        return p["number"] != 1 or bool(p["captions"])
    if "CLOSING" in ident:
        return bool(by_role(p, "closing_question")) or p["number"] == p["total"]
    return True


def validate(
    pdf_path,
    output_dir,
    *,
    tex_path=None,
    profile="generic",
    rules_path=ROOT / "rules.yaml",
    word_budget=None,
):
    started = time.perf_counter()
    rows = rules(rules_path)
    if word_budget is not None:
        if not math.isfinite(word_budget) or word_budget < 1:
            raise ValueError("Word budget must be finite and positive")
        for r in rows:
            if r["id"] == "TEXT-WORD-BUDGET":
                r["thresholds"]["max_units"] = word_budget
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    tex = Path(tex_path).read_text() if tex_path else None
    pages = []
    errors = []
    with pdf.open(pdf_path) as doc:
        if doc.needs_pass:
            raise ValueError("Encrypted PDF requires a decrypted input")
        if not len(doc):
            raise ValueError("Empty PDF")
        total = len(doc)
        for i, page in enumerate(doc, 1):
            try:
                pages.append(extract(page, i, len(doc), profile, tex))
            except Exception as exc:  # noqa: BLE001 -- preserve page failure evidence
                errors.append({"page": i, "error": f"{type(exc).__name__}: {exc}"})
        ctx = build_context(pages, rows, doc.get_toc())
        findings = []
        coverage = []
        manual = defaultdict(list)
        for p in pages:
            ctx["page"] = doc[p["number"] - 1]
            for r in rows:
                if not applicable(r, p, profile):
                    coverage.append(
                        {
                            "rule_id": r["id"],
                            "page": p["number"],
                            "status": "NOT_APPLICABLE",
                            "reason": "Different declared template or structural page role.",
                        }
                    )
                    continue
                if r["mode"] == "judged":
                    if r["id"] in {"TEXT-NO-LABEL-PHRASES", "TEXT-NO-ENDING-DISCLAIMER"}:
                        for hit in screen_prose(p, r, ctx):
                            findings.append({**hit, "rule_id": r["id"], "mode": "judged", "rule": r["rule"]})
                    manual[r["id"]].append(p["number"])
                    coverage.append(
                        {"rule_id": r["id"], "page": p["number"], "status": "REVIEW"}
                    )
                    continue
                try:
                    hits = globals()[r["detector"]](p, r, ctx)
                except Exception as exc:  # noqa: BLE001 -- failed checks must not pass
                    errors.append(
                        {
                            "page": p["number"],
                            "rule_id": r["id"],
                            "error": f"{type(exc).__name__}: {exc}",
                        }
                    )
                    hits = []
                    coverage.append(
                        {"rule_id": r["id"], "page": p["number"], "status": "ERROR"}
                    )
                    continue
                for hit in hits:
                    findings.append(
                        {
                            **hit,
                            "rule_id": r["id"],
                            "mode": r["mode"],
                            "rule": r["rule"],
                        }
                    )
                if r["mode"] == "partial":
                    manual[r["id"]].append(p["number"])
                status = (
                    "FAIL"
                    if any(x["status"] == "FAIL" for x in hits)
                    else "REVIEW"
                    if r["mode"] == "partial" or hits
                    else "PASS"
                )
                coverage.append(
                    {"rule_id": r["id"], "page": p["number"], "status": status}
                )
    failures = [f for f in findings if f["status"] == "FAIL"]
    review_hits = [f for f in findings if f["status"] == "REVIEW"]
    auto_status = "ERROR" if errors else "FAIL" if failures else "PASS"
    overall = (
        "ERROR"
        if errors
        else "FAIL"
        if failures
        else "REVIEW"
        if manual or review_hits
        else "PASS"
    )
    checklist = [
        {
            "rule_id": r["id"],
            "mode": r["mode"],
            "pages": manual[r["id"]],
            "check": r["review"],
            "thresholds": r["thresholds"],
        }
        for r in rows
        if manual[r["id"]]
    ]
    report = {
        "schema": "generic-deck-report-v1",
        "verdict": overall,
        "auto_verdict": auto_status,
        "input": {
            "pdf": str(Path(pdf_path).resolve()),
            "sha256": hashlib.sha256(Path(pdf_path).read_bytes()).hexdigest(),
            "tex_sha256": hashlib.sha256(Path(tex_path).read_bytes()).hexdigest()
            if tex_path
            else None,
        },
        "profile": profile,
        "effective_thresholds": {r["id"]: r["thresholds"] for r in rows},
        "page_count": total,
        "measured_pages": len(pages),
        "elapsed_seconds": round(time.perf_counter() - started, 4),
        "rules_sha256": hashlib.sha256(Path(rules_path).read_bytes()).hexdigest(),
        "rule_counts": dict(Counter(r["mode"] for r in rows)),
        "detector_count": len({r["detector"] for r in rows if r["detector"]}),
        "failure_count": len(failures),
        "review_hit_count": len(review_hits),
        "findings": findings,
        "human_checklist": checklist,
        "coverage": coverage,
        "errors": errors,
        "policy": {
            "no_model_calls": True,
            "unreviewed_is_not_pass": True,
            "caption_role_inference": "Caption text checks cover identified captions; CAP-REQUIRED and ROLE-EXACTLY-ONE require role review.",
            "author_detection": "Byline presence is inferred from visible text shape; identity is never verified.",
            "calibration": "Template thresholds and documented configurable defaults only; no positive-deck identity whitelist.",
        },
    }
    (output_dir / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    (output_dir / "report.md").write_text(markdown(report))
    return report


def escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def markdown(r):
    lines = [
        f"总判定：**{r['verdict']}**；自动检查：**{r['auto_verdict']}**。",
        f"共 {r['page_count']} 页，测量 {r['measured_pages']} 页；自动失败 {r['failure_count']} 项；耗时 {r['elapsed_seconds']:.2f} 秒。",
        "自动检查无失败后，仍须完成下列人判；本次未调用模型。",
        "",
        "| 规则 | 页 | 失败证据 |",
        "|---|---:|---|",
    ]
    for f in r["findings"]:
        if f["status"] == "FAIL":
            lines.append(f"| {f['rule_id']} | {f['page']} | {escape(f['evidence'])} |")
    if not r["failure_count"]:
        lines.append("| — | — | 未发现自动失败。 |")
    if r["errors"]:
        lines += ["", "检测错误（不算通过）：", ""] + [
            f"- 第 {e['page']} 页：{escape(e['error'])}" for e in r["errors"]
        ]
    lines += [
        "",
        "人判清单（每条所列的每一页均需查看）：",
        "",
        "| 规则 | 页 | 逐页检查内容 |",
        "|---|---|---|",
    ]
    for c in r["human_checklist"]:
        lines.append(
            f"| {c['rule_id']} | {page_ranges(c['pages'])} | {escape(c['check'])} |"
        )
    lines += ["", "机械初筛提示：", "", "| 规则 | 页 | 证据 |", "|---|---:|---|"]
    groups = defaultdict(list)
    for f in r["findings"]:
        if f["status"] == "REVIEW":
            groups[(f["rule_id"], f["page"])].append(f)
    for (rule_id, page), hits in groups.items():
        more = (
            f"（另 {len(hits) - 1} 项，完整证据见 report.json）"
            if len(hits) > 1
            else ""
        )
        if rule_id in {"CAP-NATURAL-SENTENCE", "TEXT-NO-LABEL-PHRASES", "TEXT-NO-ENDING-DISCLAIMER"}:
            for hit in hits:
                candidate = hit["details"].get("text", "")
                lines.append(f"| {rule_id} | {page} | {escape(hit['evidence'])} {escape(candidate)} |")
        else:
            lines.append(f"| {rule_id} | {page} | {escape(hits[0]['evidence'])}{more} |")
    return "\n".join(lines) + "\n"


def page_ranges(pages):
    groups = []
    for n in sorted(set(pages)):
        if groups and groups[-1][-1] + 1 == n:
            groups[-1].append(n)
        else:
            groups.append([n])
    return ", ".join(str(g[0]) if len(g) == 1 else f"{g[0]}–{g[-1]}" for g in groups)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--tex", type=Path)
    parser.add_argument("--profile", choices=["generic", "v19"], default="generic")
    parser.add_argument("--rules", type=Path, default=ROOT / "rules.yaml")
    parser.add_argument("--word-budget", type=float)
    args = parser.parse_args()
    try:
        r = validate(
            args.pdf,
            args.out,
            tex_path=args.tex,
            profile=args.profile,
            rules_path=args.rules,
            word_budget=args.word_budget,
        )
    except Exception as exc:  # noqa: BLE001 -- the CLI must emit an ERROR report
        args.out.mkdir(parents=True, exist_ok=True)
        error = {
            "schema": "generic-deck-report-v1",
            "verdict": "ERROR",
            "auto_verdict": "ERROR",
            "errors": [{"error": f"{type(exc).__name__}: {exc}"}],
        }
        (args.out / "report.json").write_text(
            json.dumps(error, ensure_ascii=False, indent=2) + "\n"
        )
        (args.out / "report.md").write_text(
            f"总判定：**ERROR**；检测未完成。\n\n{exc}\n"
        )
        print(json.dumps(error, ensure_ascii=False))
        return 3
    print(
        json.dumps(
            {
                k: r[k]
                for k in [
                    "verdict",
                    "auto_verdict",
                    "page_count",
                    "failure_count",
                    "review_hit_count",
                    "elapsed_seconds",
                ]
            },
            ensure_ascii=False,
        )
    )
    return 3 if r["verdict"] == "ERROR" else 2 if r["failure_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
