import os
import tempfile

base = tempfile.mkdtemp()
os.makedirs(os.path.join(base, "data"))

path = os.path.join(base, "data", "scores.csv")
with open(path, "w") as f:
    f.write("name,score\nAna,95\n")

print("Exists:", os.path.exists(path))
print("Is file:", os.path.isfile(path))
print("File name:", os.path.basename(path))
print("Extension:", os.path.splitext(path)[1])
print("Size:", os.path.getsize(path), "bytes")

print()

for root, dirs, files in os.walk(base):
    print(os.path.relpath(root, base), dirs, files)