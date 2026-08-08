from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = "<td>10.05.2026</td><td>5.01</td><td>29:22</td><td>5:51</td>"
new = "<td>10.05.2025</td><td>5.01</td><td>29:22</td><td>5:51</td>"

if old in s:
    s = s.replace(old, new, 1)
elif new in s:
    raise SystemExit(0)
else:
    raise RuntimeError('Archive row 10.05 not found')

p.write_text(s, encoding='utf-8')
