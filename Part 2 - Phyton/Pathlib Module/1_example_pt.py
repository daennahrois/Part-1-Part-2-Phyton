from pathlib import Path

p = Path("projects") / "school" / "grades.txt"

print("Path:", p)
print("Name:", p.name)
print("Stem:", p.stem)
print("Suffix:", p.suffix)
print("Parent:", p.parent)

print("Changed suffix:", p.with_suffix(".csv"))