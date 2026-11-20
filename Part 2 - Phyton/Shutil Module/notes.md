# SHUTIL MODULE

## Definition

The Shutil Module is a built-in Python module used for high-level file operations. The name is short for shell utilities. While the OS and Pathlib modules are good for small jobs, Shutil handles the bigger ones: copying files, copying whole folders, moving files, creating zip files, and deleting a folder together with everything inside it.

## Importing the Module

```python
import shutil
```

## Common Functions and Uses

- `shutil.copy()` – Copies a file.
- `shutil.copytree()` – Copies a whole folder with everything inside.
- `shutil.move()` – Moves a file or folder to a new place.
- `shutil.rmtree()` – Deletes a folder together with everything inside.
- `shutil.disk_usage()` – Shows the total, used, and free space of the disk.

## Code Examples

### Example 1: Copy Files

```python
import shutil
import tempfile
from pathlib import Path

base = Path(tempfile.mkdtemp())

source = base / "report.txt"
source.write_text("Quarterly report")

shutil.copy(source, base / "report_copy.txt")
shutil.copy2(source, base / "report_copy2.txt")

backup = base / "backup"
backup.mkdir()
shutil.copy(source, backup)

print("Base:", sorted(p.name for p in base.iterdir()))
print("Backup:", [p.name for p in backup.iterdir()])
print("Copy content:", (base / "report_copy.txt").read_text())
```

**Sample Output:**

```
Base: ['backup', 'report.txt', 'report_copy.txt', 'report_copy2.txt']
Backup: ['report.txt']
Copy content: Quarterly report
```

**Explanation:** This program uses `shutil.copy()` to copy report.txt, and `shutil.copy2()` to copy it while keeping details like the last modified date. It also copies the file into a backup folder, where the copy keeps the name report.txt. All the copies have the same content, Quarterly report.

### Example 2: Copy a Folder and Move a File

```python
import shutil
import tempfile
from pathlib import Path

base = Path(tempfile.mkdtemp())

project = base / "project"
project.mkdir()
(project / "main.py").write_text("print('hi')")
(project / "data.csv").write_text("a,b")

shutil.copytree(project, base / "project_backup")
print("Backup:", sorted(p.name for p in (base / "project_backup").iterdir()))

archive = base / "archive"
archive.mkdir()

shutil.move(base / "project_backup" / "data.csv", archive / "data.csv")
print("Archive:", [p.name for p in archive.iterdir()])
print("Backup now:", [p.name for p in (base / "project_backup").iterdir()])
```

**Sample Output:**

```
Backup: ['data.csv', 'main.py']
Archive: ['data.csv']
Backup now: ['main.py']
```

**Explanation:** This program uses `shutil.copytree()` to copy the whole project folder into project_backup, and `shutil.move()` to move data.csv from project_backup into archive. After the move, archive has data.csv and project_backup has only main.py, because a move takes the file out of the old place.

### Example 3: Zip a Folder, Delete It, and Check Disk Space

```python
import shutil
import tempfile
from pathlib import Path

base = Path(tempfile.mkdtemp())

project = base / "project"
project.mkdir()
(project / "main.py").write_text("print('hi')")
(project / "data.csv").write_text("a,b")

zip_path = shutil.make_archive(str(base / "project_backup"), "zip", project)
print("Zip created:", Path(zip_path).name)

shutil.rmtree(project)
print("Project folder exists:", project.exists())

total, used, free = shutil.disk_usage(base)
print("Free space is more than zero:", free > 0)
```

**Sample Output:**

```
Zip created: project_backup.zip
Project folder exists: False
Free space is more than zero: True
```

**Explanation:** This program uses `shutil.make_archive()` to turn the project folder into project_backup.zip, `shutil.rmtree()` to delete the folder with all its files, and `shutil.disk_usage()` to get the total, used, and free disk space. After the delete, `project.exists()` prints False, and the free space check prints True.

## Advantages

- Built in to Python, so no installation is needed.
- Copies and moves files and whole folders in one line.
- Works well together with the OS and Pathlib modules.

## Disadvantages

- Copying or zipping very large folders can take a long time.
- Not meant for small jobs like checking a file. The OS and Pathlib modules are better for that.

## Conclusion

The Shutil Module handles the bigger file jobs that the OS and Pathlib modules do not do easily. In these examples, we copied files, copied a whole folder and moved a file, and zipped a folder, deleted it, and checked the disk space.Together, the OS, Pathlib, and Shutil modules give us the main tools for managing files and folders in Python, which is the base for backups, file organizers, and automation scripts.
