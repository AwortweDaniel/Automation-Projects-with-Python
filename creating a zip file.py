from pathlib import Path
import zipfile

root_dir = Path("creating a zip file")
achieve_path = root_dir / Path("achieve.zip")

with zipfile.ZipFile(achieve_path, "w") as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink()