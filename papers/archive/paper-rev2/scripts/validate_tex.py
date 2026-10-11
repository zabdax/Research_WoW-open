"""Structural validation of the revised paper package.

Checks: brace balance, environment matching, label/ref consistency,
citation keys against references.bib, figure file existence, and stale
text patterns from the pre-revision draft.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4] / "papers" / "archive" / "paper-rev1"
tex = (ROOT / "main.tex").read_text(encoding="utf-8")
bib = (ROOT / "references.bib").read_text(encoding="utf-8")
problems = []

# 1. Brace balance (ignore escaped braces)
t = re.sub(r"\\[{}]", "", tex)
if t.count("{") != t.count("}"):
    problems.append(f"Brace imbalance: {t.count('{')} open vs {t.count('}')} close")

# 2. Environment matching
begins = re.findall(r"\\begin\{(\w+\*?)\}", tex)
ends = re.findall(r"\\end\{(\w+\*?)\}", tex)
from collections import Counter
cb, ce = Counter(begins), Counter(ends)
for env in set(cb) | set(ce):
    if cb[env] != ce[env]:
        problems.append(f"Environment mismatch: {env}: {cb[env]} begin / {ce[env]} end")

# 3. Labels vs refs
labels = set(re.findall(r"\\label\{([^}]+)\}", tex))
refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", tex))
for r in sorted(refs - labels):
    problems.append(f"\\ref to undefined label: {r}")
for l in sorted(labels - refs):
    problems.append(f"Unused label (informational): {l}")

# 4. Citations vs bib entries
keys_used = set()
for m in re.finditer(r"\\cite[a-z]*\s*(\[[^\]]*\])*\{([^}]+)\}", tex):
    for k in m.group(2).split(","):
        keys_used.add(k.strip())
keys_bib = set(re.findall(r"@\w+\{([^,\s]+),", bib))
for k in sorted(keys_used - keys_bib):
    problems.append(f"Citation key missing from references.bib: {k}")
for k in sorted(keys_bib - keys_used):
    problems.append(f"Bib entry never cited (informational): {k}")

# 5. Figures referenced exist
for fig in set(re.findall(r"\\plotone\{([^}]+)\}", tex)):
    if not (ROOT / "figures" / fig).exists():
        problems.append(f"Missing figure file: {fig}")

# 6. Stale patterns
for pat, desc in [
    (r"MAP likelihood", "pre-revision 'MAP likelihood' (allowed only in terminology note)"),
    (r"1\.4--1\.6\\%", "stale emulator range"),
    (r"1\.42\\%", "stale MC value"),
    (r"in preparation", "stale 'in preparation' bib note in text"),
    (r"3\.06\\times10\^\{13\}", "old incorrect EIRP constant"),
]:
    hits = [(tex[:m.start()].count("\n") + 1) for m in re.finditer(pat, tex)]
    if hits:
        problems.append(f"Pattern '{desc}' found at lines {hits}")

print("Citation keys used:", len(keys_used))
print("Bib entries:", len(keys_bib))
if problems:
    print("\nPROBLEMS:")
    for p in problems:
        print(" -", p)
else:
    print("\nAll structural checks passed.")
