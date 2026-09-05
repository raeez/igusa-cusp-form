#!/usr/bin/env python3
"""Exercise local Makefile failure gates with harmless fake TeX tools."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FAKE = r'''#!/usr/bin/env python3
import os
from pathlib import Path
import sys
kind = Path(sys.argv[0]).name
mode = os.environ.get("FIXTURE_MODE", "success")
if kind == "fake-tex":
    out = Path(next(x.split("=", 1)[1] for x in sys.argv if x.startswith("-output-directory=")))
    stem = Path(sys.argv[-1]).stem
    if mode == "tex-fail":
        print("Fixture TeX failed without a conventional error marker")
        sys.exit(7)
    if mode != "missing-pdf":
        (out / (stem + ".pdf")).write_text("fresh fixture PDF")
        (out / (stem + ".idx")).write_text("fixture index")
    if mode == "fatal-zero":
        print("! Fixture error despite zero status")
    if mode == "undefined":
        print("LaTeX Warning: Reference `fixture' undefined")
elif kind == "fake-bib":
    if mode == "bib-fail":
        print("Fixture bibliography failure")
        sys.exit(8)
    if mode == "bib-zero":
        print("I couldn't open database file fixture.bib")
elif kind == "fake-index" and mode == "index-fail":
    print("Fixture index failure")
    sys.exit(9)
'''


class LocalBuildRecipes(unittest.TestCase):
    def exercise(self, target, mode, absolute=False):
        with tempfile.TemporaryDirectory(prefix="igusa-build-fixture-") as temp:
            root = Path(temp)
            shutil.copy2(ROOT / "Makefile", root / "Makefile")
            for directory in ["platonic", "standalone", "out"]:
                (root / directory).mkdir()
            for name in ["main.tex", "proj.bib", "platonic/main.tex", "standalone/sample.tex"]:
                (root / name).write_text("fixture")
            for kind in ["tex", "bib", "index"]:
                tool = root / ("fake-" + kind)
                tool.write_text(FAKE)
                tool.chmod(0o755)
            artifact = root / "out" / {"all": "main.pdf", "fast": "main.pdf", "platonic": "platonic.pdf", "standalone": "sample.pdf"}[target]
            artifact.write_text("stale fixture PDF")
            (root / "platonic/main.pdf").write_text("stale source PDF")
            overrides = ["OUT_DIR=" + str(root / "out"), "LOG_DIR=" + str(root / ".build_logs")] if absolute else []
            result = subprocess.run(
                ["make", "-B", target, "TEX=" + str(root / "fake-tex"),
                 "BIBTEX=" + str(root / "fake-bib"), "MAKEINDEX=" + str(root / "fake-index")] + overrides,
                cwd=root, env={**os.environ, "FIXTURE_MODE": mode},
                text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            if mode == "success":
                self.assertEqual(result.returncode, 0, result.stdout)
                self.assertEqual(artifact.read_text(), "fresh fixture PDF")
            else:
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertFalse(artifact.exists(), result.stdout)

    def test_local_recipes(self):
        for target in ["all", "fast", "platonic", "standalone"]:
            modes = ["success", "tex-fail", "missing-pdf", "fatal-zero"]
            if target in ["all", "platonic"]:
                modes += ["bib-fail", "bib-zero"]
            if target in ["all", "standalone"]:
                modes += ["index-fail"]
            if target in ["platonic", "standalone"]:
                modes += ["undefined"]
            for mode in modes:
                for absolute in [False, True]:
                    with self.subTest(target=target, mode=mode, absolute=absolute):
                        self.exercise(target, mode, absolute)


if __name__ == "__main__":
    unittest.main()
