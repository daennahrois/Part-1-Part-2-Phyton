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