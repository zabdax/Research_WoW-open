"""One-off: inspect PDF page breaks (p1/p2 content)."""
import sys
src = sys.argv[1] if len(sys.argv) > 1 else "C:/Windows/Temp/opencode/ms.txt"
t = open(src, encoding="utf-8", errors="replace").read()
pages = t.split("\x0c")
out = []
out.append("NPAGES %d" % len(pages))
for i in (0, 1):
    body = pages[i].strip().replace("\n", " ")
    out.append("---P%d HEAD---" % (i + 1))
    out.append(body[:400])
    out.append("---P%d TAIL---" % (i + 1))
    out.append(body[-400:])
open("C:/Windows/Temp/opencode/pages_out.txt", "w", encoding="ascii",
     errors="backslashreplace").write("\n".join(out))
print("wrote pages_out.txt")
