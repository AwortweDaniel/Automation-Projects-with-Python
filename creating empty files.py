from pathlib import Path

root_dir = Path("creating empty files")

for i in range(2, 16):
    filename = str(i) + ".txt"
    filepath = root_dir/ Path(filename)
    filepath.touch()