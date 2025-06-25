import os

years = list(range(2015,2025))
days = list(range(1,26))

home_dir = "/data/data/com.termux/files/home/code/Advent-of-Code"
s1 = "solution_1.py"
s2 = "solution_2.py"
s1_copy = "solution_1_copy.py"
s2_copy = "solution_2_copy.py"

for year in years:
  for day in days:
    day_folder = os.path.join(home_dir, f"{year}", f"day_{day:02}")
    s1_path = os.path.join(day_folder, s1)
    s2_path = os.path.join(day_folder, s2)
    s1_copy_path = os.path.join(day_folder, s1_copy)
    s2_copy_path = os.path.join(day_folder, s2_copy)

    s2_title = f"# Solution 2 - Advent of Code {year}, Day {day}\n"

#    with open(s1_path, "r") as f:
#      s1_lines = f.readlines()

#    if s1_lines[1] == "\n":
#      new_lines = [s1_lines[0]]
#      new_lines += s1_lines[2:]
#      with open(s1_copy_path, "w") as f:
#        f.writelines(new_lines)

    with open(s2_path, "r") as f:
      s2_lines = f.readlines()
    new_lines = [s2_title]
    if s2_lines[1] == "\n":
      new_lines += s2_lines[2:]
    else:
      new_lines += s2_lines[1:]
    with open(s2_copy_path, "w") as f:
      f.writelines(new_lines)
