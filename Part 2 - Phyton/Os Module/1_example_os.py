import os
import tempfile

base = tempfile.mkdtemp()

print("Operating system:", os.name)
print("Current folder:", os.getcwd())

print("Items:", os.listdir(base))

with open(os.path.join(base, "a.txt"), "w") as f:
    f.write("Hello")

print("Items:", os.listdir(base))