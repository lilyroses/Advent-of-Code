import os


home_dir = "/data/data/com.termux/files/home/code/Advent-of-Code"
s1_copy = "solution_1_copy.py"
s2_copy = "solution_2_copy.py"

for year in range(2015,2025):
  for day in range(1,26):
    day_folder = os.path.join(home_dir, f"{year}", f"day_{day:02}")
    s1_copy_path = os.path.join(day_folder, s1_copy)
    s2_copy_path = os.path.join(day_folder, s2_copy)

    if os.path.exists(s1_copy_path):
      with open(s1_copy_path, "r") as f:
        lines = f.readlines()
      if lines[1] == "\n":
        print(f"Needs fix: {s1_copy_path}")

    if os.path.exists(s2_copy_path):
      with open(s2_copy_path, "r") as f:
        lines = f.readlines()
      if lines[1] == "\n":
        print(f"Needs fix: {s2_copy_path}")
