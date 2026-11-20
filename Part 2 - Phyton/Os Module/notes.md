# OS MODULE

## Definition

The OS Module is a built-in Python module used to interact with the operating system, such as Windows, Mac, or Linux. The name OS stands for operating system. It allows programmers to do in code what we usually do by hand in File Explorer.The OS Module is useful when a program needs to organize, check, or clean up many files automatically. Because it is built in, we only need to import it, with no installation.

## Importing the Module

```python
import os
```

## Common Functions and Uses

- `os.getcwd()` – Gets the folder where the program is running.
- `os.listdir()` – Lists the names of the files and folders inside a folder.
- `os.mkdir()` – Creates one folder.
- `os.rename()` – Renames a file or a folder.
- `os.remove()` – Deletes a file.
- `os.rmdir()` – Deletes an empty folder.
- `os.path` – Checks a path: exists, file name, extension, and size.

## Code Examples

### Example 1: See Where We Are and What Is Inside a Folder

```python
import os
import tempfile

base = tempfile.mkdtemp()

print("Operating system:", os.name)
print("Current folder:", os.getcwd())

print("Items:", os.listdir(base))

with open(os.path.join(base, "a.txt"), "w") as f:
    f.write("Hello")

print("Items:", os.listdir(base))
```

**Sample Output:**

```
Operating system: posix
Current folder: /home/user/lesson
Items: []
Items: ['a.txt']
```

**Explanation:** This program uses `os.name` to show the type of operating system, `os.getcwd()` to show the current working folder, and `os.listdir()` to list the items inside a folder. It first prints an empty list because the temporary folder is new, then it creates a.txt with `os.path.join()` and lists the folder again to show the new file.

### Example 2: Create, Rename and Delete

```python
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
```

**Sample Output:**

```
Items: ['photos', 'school']
After rename: ['python_notes.txt']
After delete: ['photos']
```

**Explanation:** This program uses `os.mkdir()` to create the school folder and `os.makedirs()` to create photos with 2026 inside it. It then uses `os.rename()` to change notes.txt to python_notes.txt, `os.remove()` to delete the file, and `os.rmdir()` to delete the empty school folder, so only photos is left.

### Example 3: Check a Path and Walk Through Folders

```python
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
```

**Sample Output:**

```
Exists: True
Is file: True
File name: scores.csv
Extension: .csv
Size: 18 bytes

. ['data'] []
data [] ['scores.csv']
```

**Explanation:** This program uses `os.path.exists()` and `os.path.isfile()` to check that the file is there, `os.path.basename()` to get the file name, `os.path.splitext()` to get the extension, and `os.path.getsize()` to get the size in bytes. It then uses `os.walk()` to go through every folder and show the folders and files inside each one.

## Advantages

- Built in to Python, so no installation is needed.
- Works on Windows, Mac, and Linux.
- Can create, rename, and delete files and folders.
- Helps check a file before using it, like its name, extension, and size.

## Disadvantages

- `os.remove()` and `os.rmdir()` delete things for good, with no recycle bin.
- Paths are plain text, so the code is longer than with Pathlib.
- Has no simple way to copy files or folders. Shutil is better for that.

## Conclusion

The OS Module lets Python talk to the operating system. In these examples, we checked the current folder and listed its items, created, renamed, and deleted files and folders, and checked a file and walked through every folder. Remember that `os.remove()` and `os.rmdir()` delete things for good, so we should use them carefully.