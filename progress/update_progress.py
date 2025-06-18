import json
import sys
from datetime import datetime

PROGRESS_DATA_FILE = "progress_data.json"

with open(PROGRESS_DATA_FILE, "r") as f:
  PROGRESS_DATA = json.load(f)


current = datetime.today()
year_end = current.year
if not current.month == 12:
  year_end -= 1


def invalid_num_parameters_error():
  print(f"\nError: Invalid number of parameters (required: year, day, solution_part)")
  sys.exit()

def invalid_type(parameter):
  print(f"\nError: Invalid {parameter} (must be a number).")
  sys.exit()

def out_of_range(parameter):
  print(f"\nError: {parameter} out of range.")
  sys.exit()

def update_progress(year, day, solution_part):
  PROGRESS_DATA[year][day] = solution_part
  with open(PROGRESS_DATA_FILE, "w") as f:
    json.dump(PROGRESS_DATA, f)


if len(sys.argv) != 4:
  invalid_num_parameters_error()

year, day, solution_part = sys.argv[1:]

try:
  year = int(year)
except ValueError:
  invalid_type("year")
if year not in range(2015, year_end+1):
  out_of_range("year")

try:
  day = int(day)
except ValueError:
  invalid_type("day")
if day not in range(1, 26):
  out_of_range("day")

try:
  solution_part = int(solution_part)
except ValueError:
  invalid_type("solution_part")
if solution_part not in [0,1,2]:
  out_of_range("solution_part")


update_progress(str(year), str(day), solution_part)

