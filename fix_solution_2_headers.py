# fix_solution_2_headers.property

"""NOTE: ALREADY RUN ON MY FILES; `create_aoc.py` HAS BEEN FIXED, INCLUDED FOR POSTERITY. 
"""

HOME_DIR = "/home/lilyroses/code/Advent-of-Code"
year_folders = [str(year) for year in range(2015, 2025)]
day_folders = [f"day_{day:02}" for day in range(1,26)]

file_name = "solution_2.py"
copy_file_name = "solution_2-2.py"

for year_folder in year_folders:
    for day_folder in day_folders:
        path = f"{HOME_DIR}/{year_folder}/{day_folder}/{file_name}"
        copy_path = f"{HOME_DIR}/{year_folder}/{day_folder}/{copy_file_name}"
        with open(path, "r") as f:
            lines = f.readlines()
        header = lines[0]
        items = header.split()
        new_items = items[:2]
        new_items.append("2")
        new_items += items[3:]
        new_header = " ".join(new_items)
        new_lines = [new_header, "\n"]
        new_lines += lines[1:]
        with open(copy_path, "w") as f:
            f.writelines(new_lines)
