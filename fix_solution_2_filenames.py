# fix_solution_2_filenames.py

HOME_DIR = "/home/lilyroses/code/Advent-of-Code"
year_folders = [str(year) for year in range(2015, 2025)]
day_folders = [f"day_{day:02}" for day in range(1,26)]

old_file_name = "solution_2-2.py"
new_file_name = "solution_2.py"

for year_folder in year_folders:
    for day_folder in day_folders:
        old_file_name_path = f"{HOME_DIR}/{year_folder}/{day_folder}/{old_file_name}"
        new_file_name_path = f"{HOME_DIR}/{year_folder}/{day_folder}/{new_file_name}"
        with open(old_file_name_path, "r") as f:
            lines = f.readlines()
        with open(new_file_name_path, "w") as f:
            f.writelines(lines)
