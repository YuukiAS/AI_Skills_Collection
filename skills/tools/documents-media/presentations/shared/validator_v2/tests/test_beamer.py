from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
import unittest

from presentations_validator_v2.io import canonical, sha256
from presentations_validator_v2.layout import validate
from presentations_validator_v2.render import Render, document
from presentations_validator_v2.schemas import report

from test_layout import CONTRACT


class PublicBeamerControls(unittest.TestCase):
    @unittest.skipUnless(shutil.which("xelatex"), "XeLaTeX not available")
    def test_unrelated_teaching_and_research_renders(self):
        for fixture in (Path(__file__).parent / "fixtures").glob("*.tex"):
            with self.subTest(fixture=fixture.stem), TemporaryDirectory() as tmp:
                root = Path(tmp)
                local = root / fixture.name
                local.write_bytes(fixture.read_bytes())
                font = subprocess.check_output(
                    ["kpsewhich", "texgyretermes-regular.otf"], text=True
                ).strip()
                shutil.copyfile(font, root / Path(font).name)
                invocation = subprocess.run(
                    ["xelatex", "-no-shell-escape", "-halt-on-error", "-interaction=batchmode",
                     local.name], cwd=root, capture_output=True, check=False,
                )
                log = (root / f"{fixture.stem}.log").read_text()
                self.assertEqual(invocation.returncode, 0, "\n".join(log.splitlines()[-30:]))
                pdf = (root / f"{fixture.stem}.pdf").read_bytes()
                manifest = {"pdf_sha256": sha256(pdf), "entry_source": "entry", "sources": [
                    {"id": "entry", "path": fixture.name, "role": "authored",
                     "sha256": sha256(local.read_bytes())}
                ]}
                with document(pdf) as doc:
                    native = Render.extract(doc[0])
                self.assertEqual(len(native.lines), 2)
                self.assertEqual(len(native.drawings), 1)
                obj_map = {
                    "pdf_sha256": sha256(pdf), "source_manifest_sha256": sha256(canonical(manifest)),
                    "pages": [{"id": "content", "index": 0, "section": "one", "spacing": [],
                               "footer_exempt": True, "objects": [
                                   {"id": f"paragraph-{i}", "role": "paragraph", "lines": [i]}
                                   for i in range(len(native.lines))
                               ] + [{"id": "canvas", "role": "background", "drawings": [0]}]}],
                }
                rows, identity = validate(CONTRACT, pdf, manifest, obj_map, root)
                evidence = report(rows, **identity)
                self.assertEqual(evidence["state"], "DETERMINISTIC_NO_FAIL_REVIEW_REQUIRED", evidence)
