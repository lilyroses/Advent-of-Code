import json
import sys
from datetime import datetime


PROGRESS_DATA_FILE = "progress_data.json"
with open(PROGRESS_DATA_FILE, "r") as f:
  PROGRESS_DATA = json.load(f)


current_year = datetime.today().year


def update_progress(year, day, solution_part):
  
  if year not in PROGRESS_DATA:
    PROGRESS_DATA[year] = {}
  
  PROGRESS_DATA[year][day] = solution_part
  with open(PROGRESS_DATA_FILE, "w") as f:
    json.dump(PROGRESS_DATA, f)

if len(sys.argv) != 4:
  print(f"\nError: Invalid number of parameters (required: year, day, solution_part)")
  sys.exit()

year, day, solution_part = sys.argv[1:]

try:
  year = int(year)
except ValueError:
  print("Error: year must be integer value")
  sys.exit()
if year not in range(2015, current_year+1):
  print(f"\nError: year out of range.")
  sys.exit()

try:
  day = int(day)
except ValueError:
  print("Error: day must be integer value.")
if day not in range(1, 26):
  out_of_range("day")

try:
  solution_part = int(solution_part)
except ValueError:
  invalid_type("solution_part")
if solution_part not in [0,1,2]:
  out_of_range("solution_part")


update_progress(str(year), str(day), solution_part)

