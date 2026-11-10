#!/usr/bin/env python3
"""Render the specified D2/ELK lanes and route cross-lane connections.

D2 places both vertical lanes inside a horizontal grid. Its cross-grid edges
are straight, so these edges are routed in the empty handoff/top gutters.
This changes neither topology, labels, colors nor shapes. All downloaded tools,
fonts, intermediate SVG and fontconfig caches remain in the ignored .cache/.
"""
from __future__ import annotations

import base64
import os
from pathlib import Path
import re
import subprocess
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CACHE = ROOT / '.cache/assurance-diagram'
D2 = CACHE / 'tools/d2-v0.9.0/bin/d2'
FONTS = CACHE / 'fonts'
NAME = 'ASSURANCE_PROCESS_20261109'
NS = '{http://www.w3.org/2000/svg}'


def main() -> None:
    fonts = []
    for kind, weight in [('regular', 'Regular'), ('bold', 'Bold'),
                         ('semibold', 'Bold'), ('italic', 'Regular')]:
        fonts += [f'--font-{kind}', str(FONTS / f'NotoSansSC-{weight}.ttf')]
    raw = CACHE / 'layout.svg'
    subprocess.run([str(D2), '--layout=elk', '--pad', '40', '--scale', '1',
                    '--elk-nodeNodeBetweenLayers', '50',
                    '--elk-edgeNodeBetweenLayers', '20', *fonts,
                    str(HERE / f'{NAME}.d2'), str(raw)], check=True)
    tree = ET.parse(str(raw))
    root = tree.getroot()
    inner = root.find(NS + 'svg')
    assert inner is not None

    def shape(key):
        code = base64.b64encode(key.encode()).decode()
        return next(x for x in inner.xpath('.//*[@class]')
                    if code in x.get('class', '').split())

    def rect(key):
        item = shape(key).find('.//' + NS + 'rect')
        assert item is not None, key
        return tuple(float(item.get(k)) for k in ('x', 'y', 'width', 'height'))

    def edge(source, target, index=0):
        return shape(f'({source} -&gt; {target})[{index}]')

    def label(group, x, y):
        text = group.find(NS + 'text')
        assert text is not None
        text.set('x', str(x))
        text.set('y', str(y))
        for span in text.findall(NS + 'tspan'):
            span.set('x', str(x))

    def route(group, points):
        path = group.find(NS + 'path')
        assert path is not None
        path.set('d', 'M ' + ' L '.join(f'{x:g} {y:g}' for x, y in points))
        path.attrib.pop('mask', None)

    lx, ly, lw, lh = rect('design')
    hx, hy, hw, hh = rect('handoff')
    rx, ry, rw, rh = rect('delivery')
    dx, dy, dw, dh = rect('design.owner')
    ex, ey, ew, eh = rect('delivery.owner')
    ax, ay, aw, ah = rect('design.approve')
    doc = shape('handoff.contract')
    center_x = float(doc.find(NS + 'text').get('x'))
    path = doc.find('.//' + NS + 'path')
    old_doc_y = float(re.match(r'M\s+[-\d.]+\s+([-\d.]+)', path.get('d'))[1])
    doc_h, doc_w = 285.0, 490.0
    doc_y = (lh - doc_h) / 2
    doc.set('transform', f'translate(0 {doc_y - old_doc_y:g})')
    left, right = center_x-doc_w/2, center_x+doc_w/2
    mid_y = doc_y + doc_h/2
    gutter_left = (lx+lw+hx)/2
    gutter_right = (hx+hw+rx)/2

    route(edge('design.approve', 'handoff.contract'), [
        (ax+aw+3, ay+ah/2), (gutter_left, ay+ah/2),
        (gutter_left, mid_y), (left-7, mid_y)])
    route(edge('handoff.contract', 'delivery.owner'), [
        (right+3, mid_y), (gutter_right, mid_y),
        (gutter_right, ey+eh/2), (ex-7, ey+eh/2)])

    red = edge('delivery.owner', 'design.owner', 0)
    return_x = rx+rw+65
    route(red, [(ex+ew+3, ey+eh*0.25), (return_x, ey+eh*0.25),
                (return_x, -85),
                (dx+dw/2, -85), (dx+dw/2, dy-12)])
    label(red, (dx+dw/2+ex+ew/2)/2, -230)
    orange = edge('delivery.owner', 'design.owner', 1)
    ox, tx = ex-65, dx-80
    route(orange, [(ex-3, ey+eh/2), (ox, ey+eh/2), (ox, -20),
                   (tx, -20), (tx, dy+dh/2), (dx-7, dy+dh/2)])
    label(orange, (dx+dw/2+ex+ew/2)/2, -34)

    purple = edge('design.owner', 'handoff.contract')
    px, py = lx+lw+32, doc_y+38
    route(purple, [(dx+dw+3, dy+dh*0.77), (px, dy+dh*0.77),
                   (px, py), (left-7, py)])
    label(purple, (dx+dw+px)/2, dy+dh*0.77-38)

    # Keep professional evidence outside the diagnostic node and its caption.
    qx, qy, qw, qh = rect('delivery.professional')
    evidence = shape('delivery.(professional -&gt; owner)[0]')
    evidence_x = rx+rw-25
    evidence_y = qy+qh*0.7
    route(evidence, [(qx+qw+3, evidence_y), (evidence_x, evidence_y),
                     (evidence_x, ey+eh*0.8), (ex+ew+7, ey+eh*0.8)])
    label(evidence, (qx+qw+evidence_x)/2, evidence_y-22)

    # Samples need enough length to show repeated dashes, rather than one dash.
    for name in ['normal', 'back', 'proposal', 'evidence', 'revision']:
        sample = shape(f'legend.lines.{name}.(a -&gt; b)[0]')
        path = sample.find(NS+'path')
        points = [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?', path.get('d'))]
        center = (points[0]+points[-2])/2
        y = points[1]
        route(sample, [(center-90, y), (center+90, y)])
    for group in [evidence, shape('legend.lines.evidence.(a -&gt; b)[0]')]:
        path = group.find(NS+'path')
        path.set('style', re.sub(r'stroke-dasharray:[^;]+;',
                                'stroke-dasharray:1,9;', path.get('style')))

    # Retain D2's embedded subset fonts for SVG readers; fontconfig provides
    # the same Noto Sans SC font to librsvg when writing the PNG.
    style = ET.SubElement(inner, NS + 'style')
    css = '\n'.join(inner.xpath('./*[local-name()="style"]/text()')[:-1])
    families = re.findall(r'font-family:\s*[\'"]?([^;\n\'"}]+)', css)
    families = [x.strip() for x in families if 'font-' in x]
    regular = next((x for x in families if 'font-regular' in x), 'Noto Sans SC')
    bold = next((x for x in families if 'font-bold' in x), 'Noto Sans SC')
    style.text = (
        f'.text, .text-italic {{font-family: "{regular}", "Noto Sans SC", sans-serif; font-style: normal;}}\n'
        f'.text-bold {{font-family: "{bold}", "Noto Sans SC", sans-serif; font-weight: 700;}}')

    old_w, old_h = float(root.get('width')), float(root.get('height'))
    top_pad = 300.0
    # The outer red return sits beyond the right lane: reserve its full bend
    # and stroke, then expand height as needed instead of clipping horizontally.
    view_w = max((old_h+top_pad)*1.6, old_w+200)
    view_h = view_w/1.6
    view_x = (old_w-view_w)/2
    inner.tag = NS+'g'
    for key in list(inner.attrib):
        if key != 'class':
            del inner.attrib[key]
    inner.set('transform', 'translate(40 40)')
    root.set('width', '2400')
    root.set('height', '1500')
    root.set('viewBox', f'{view_x:g} {-top_pad:g} {view_w:g} {view_h:g}')
    root.set('role', 'img')
    title = ET.Element(NS+'title')
    title.text = 'Design Assurance 与 Delivery Assurance 合并流程草案'
    root.insert(0, title)
    background = ET.Element(NS+'rect', x=str(view_x), y=str(-top_pad),
                            width=str(view_w), height=str(view_h), fill='#FFFFFF')
    root.insert(1, background)
    svg = HERE/f'{NAME}.svg'
    tree.write(str(svg), encoding='utf-8', xml_declaration=True)

    config = CACHE/'fonts.conf'
    config.write_text(f'''<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig><dir>{FONTS}</dir><cachedir>{CACHE/'font-cache'}</cachedir>
<alias><family>sans-serif</family><prefer><family>Noto Sans SC</family></prefer></alias>
</fontconfig>''')
    env = os.environ.copy()
    env['FONTCONFIG_FILE'] = str(config)
    env['XDG_CACHE_HOME'] = str(CACHE/'xdg-cache')
    subprocess.run(['rsvg-convert', '-w', '4800', '-h', '3000',
                    '-o', str(HERE/f'{NAME}.png'), str(svg)], env=env, check=True)
    print('SVG 2400×1500; PNG 4800×3000; Noto Sans SC')


if __name__ == '__main__':
    main()
