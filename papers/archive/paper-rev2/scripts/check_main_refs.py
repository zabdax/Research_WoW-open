"""One-off: cross-check main.tex (AASTeX+BiBTeX) cites/labels/refs. No PDF work."""
import re

t = open("papers/archive/paper-rev2/main.tex", encoding="utf-8").read()
b = open("papers/archive/paper-rev2/references.bib", encoding="utf-8").read()
cites = set()
for c in re.findall(r"\\cite[ptal]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", t):
    for k in c.split(","):
        cites.add(k.strip())
bibs = set(re.findall(r"@\w+\{([^,]+),", b))
refs = set(re.findall(r"\\(?:ref|nameref)\{([^}]*)\}", t))
labels = set(re.findall(r"\\label\{([^}]*)\}", t))
print("cited keys:", len(cites), "bib entries:", len(bibs))
print("cites without entry:", sorted(cites - bibs))
print("entries never cited:", sorted(bibs - cites))
print("refs without label:", sorted(refs - labels))
tab_refs = sorted(k for k in refs if k.startswith("tab:"))
tab_labels = sorted(k for k in labels if k.startswith("tab:"))
print("tab labels:", tab_labels)
print("tab refs:", tab_refs)
print("unreferenced tab labels:", sorted(set(tab_labels) - set(refs)))
sec_labels = sorted(k for k in labels if k.startswith("sec:"))
print("sec labels missing a ref:", sorted(set(sec_labels) - set(refs)))
