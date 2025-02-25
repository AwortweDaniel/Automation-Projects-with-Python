from pathlib import Path

root_dir = Path('changing-file-extension')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        new_suffix = ".csv"
        new_path = path.with_suffix(new_suffix)
        path.rename(new_path)