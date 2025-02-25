from pathlib import Path
from _datetime import datetime

root_dir = Path("adding_file_created_dates_to_file_names")
file_path = root_dir.glob('**/*')


for path in file_path:
    if path.is_file():
        created_seconds = path.stat().st_ctime
        created_time = datetime.fromtimestamp(created_seconds)
        created_date = created_time.strftime("%d-%m-%Y_%H-%M-%S")
        new_file_name = f'{created_date}_{path.name}'
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)
