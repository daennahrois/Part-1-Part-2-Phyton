# PATHLIB MODULE

## Definition

The Pathlib Module is a built-in Python module used to work with file and folder paths as objects instead of plain text. A path is the address of a file or folder on the computer, like projects/school/grades.txt. With Pathlib, we can join paths using a slash, read the parts of a path such as the name and the extension, and create, read, rename, and delete files in just one line. 

## Importing the Module

```python
from pathlib import Path
```

## Common Functions and Uses

- `Path()` – Creates a path object from a file or folder location.
- `/` – Joins the parts of a path together.
- `.name`, `.stem`, `.suffix`, `.parent` – Give the file name, the name without the extension, the extension, and the folder.
- `.write_text()` – Writes text into a file.
- `.read_text()` – Reads the text inside a file.
- `.glob()` – Finds files that match a pattern, like `*.txt`.
- `.unlink()` – Deletes a file.

## Code Examples

### Example 1: Build a Path and Read Its Parts

```python
from pathlib import Path

p = Path("projects") / "school" / "grades.txt"

print("Path:", p)
print("Name:", p.name)
print("Stem:", p.stem)
print("Suffix:", p.suffix)
print("Parent:", p.parent)

print("Changed suffix:", p.with_suffix(".csv"))
```

**Sample Output:**

```
Path: projects/school/grades.txt
Name: grades.txt
Stem: grades
Suffix: .txt
Parent: projects/school
Changed suffix: projects/school/grades.csv
```

**Explanation:** This program uses `Path()` and the slash to build a path. The properties `.name`, `.stem`, `.suffix`, and `.parent` show the file name, the name without the extension, the extension, and the folder, and `.with_suffix()` creates a new path with a different extension. The original path does not change.

### Example 2: Create a Folder, Write and Read a File

```python
from pathlib import Path
import tempfile

base = Path(tempfile.mkdtemp())

folder = base / "notes" / "python"
folder.mkdir(parents=True, exist_ok=True)

file = folder / "intro.txt"
file.write_text("Hello from pathlib!")

print("Exists:", file.exists())
print("Is file:", file.is_file())
print("Content:", file.read_text())
print("Size:", file.stat().st_size, "bytes")
```

**Sample Output:**

```
Exists: True
Is file: True
Content: Hello from pathlib!
Size: 19 bytes
```

**Explanation:** This program uses `mkdir(parents=True, exist_ok=True)` to create the folders, `write_text()` to save a message in intro.txt, and `read_text()` to read it back. It also uses `exists()` and `is_file()` to check the file, and `stat().st_size` to get its size in bytes.

### Example 3: List, Search, Rename and Delete Files

```python
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
```

**Sample Output:**

```
All items:
- a.txt
- b.txt
- c.py
Text files: ['a.txt', 'b.txt']
Renamed to: main.py
After delete: ['b.txt', 'main.py']
```

**Explanation:** This program uses `iterdir()` to list the items in a folder and `glob("*.txt")` to find only the text files. It then uses `rename()` to change c.py to main.py and `unlink()` to delete a.txt, so only b.txt and main.py are left.

## Advantages

- Short and easy to read, because paths are joined with a slash.
- Handles slashes automatically on Windows, Mac, and Linux.
- `glob()` makes it easy to find files by pattern.

## Disadvantages

- `unlink()` deletes a file for good, with no recycle bin.
- Paths are objects, so some older code needs `str(path)` to use them.
- Cannot copy files or folders by itself. Shutil is better for that.
- Needs Python 3.4 or newer.

## Conclusion

The Pathlib Module treats paths as objects, which makes file handling shorter and easier to read. In these examples, we built a path and read its parts, created a folder and wrote and read a file, and listed, searched, renamed, and deleted files. Compared with the OS Module, Pathlib needs less code, especially with the slash for joining paths and methods like `read_text()` and `glob()`. Next, the Shutil Module handles the bigger jobs, like copying whole folders.
