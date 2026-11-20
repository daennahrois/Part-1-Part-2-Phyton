from pathlib import Path
import tempfile

base = Path(tempfile.mkdtemp())

for name in ["a.txt", "b.txt", "c.py"]:
    (base / name).write_text("sample")

print("All items:")
for item in sorted(base.iterdir()):
    print("-", item.name)

print("Text files:", sorted(f.name for f in base.glob("*.txt")))

renamed = (base / "c.py").rename(base / "main.py")
print("Renamed to:", renamed.name)

(base / "a.txt").unlink()
print("After delete:", sorted(f.name for f in base.iterdir()))