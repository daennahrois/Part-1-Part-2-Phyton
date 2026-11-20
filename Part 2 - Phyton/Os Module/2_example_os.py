import os
import tempfile

base = tempfile.mkdtemp()

folder = os.path.join(base, "school")
os.mkdir(folder)
os.makedirs(os.path.join(base, "photos", "2026"))
print("Items:", sorted(os.listdir(base)))

old_path = os.path.join(folder, "notes.txt")
with open(old_path, "w") as f:
    f.write("Python notes")

new_path = os.path.join(folder, "python_notes.txt")
os.rename(old_path, new_path)
print("After rename:", os.listdir(folder))

os.remove(new_path)
os.rmdir(folder)
print("After delete:", os.listdir(base))