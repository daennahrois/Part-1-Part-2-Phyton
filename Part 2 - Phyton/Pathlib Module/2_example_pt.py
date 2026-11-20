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