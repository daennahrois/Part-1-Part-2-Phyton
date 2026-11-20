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