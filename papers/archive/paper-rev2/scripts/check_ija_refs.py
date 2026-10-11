"""One-off: cite/bibitem cross-check for a manuscript file (argv[1] or IJA default)."""
import re
import sys

path = (sys.argv[1] if len(sys.argv) > 1 else
        "papers/archive/paper-rev2/ija_manuscript/manuscript.tex")
t = open(path, encoding="utf-8").read()
cites = set(re.findall(r"\\cite[ptalt]*\{([^}]*)\}", t))
used = set()
for c in cites:
    for k in c.split(","):
        used.add(k.strip())
bibs = set(re.findall(r"\\bibitem\[[^\]]*\]\{([^}]*)\}", t))
refs = set(re.findall(r"\\ref\{([^}]*)\}", t))
labels = set(re.findall(r"\\label\{([^}]*)\}", t))
print("cited keys:", len(used), "bibitems:", len(bibs))
print("uncited entries:", sorted(bibs - used))
print("missing entries:", sorted(used - bibs))
print("broken refs:", sorted(refs - labels))
print("n refs:", len(refs), "n labels:", len(labels))
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", t, re.S)
print("abstract words:", len(m.group(1).split()))
