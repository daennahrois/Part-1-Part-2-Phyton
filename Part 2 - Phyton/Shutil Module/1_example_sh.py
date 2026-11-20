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