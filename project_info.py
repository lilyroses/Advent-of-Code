# project_info.py
from datetime import datetime


# EVENT DATE INFO
current = datetime.today()
EVENT_ONGOING = False
DAY_START = 1
DAY_END = 25
YEAR_START = 2015
YEAR_END = current.year
# event ongoing if month is Dec & day on/before 25th
if current.month == 12:
  if current.day <= 25:
    EVENT_ONGOING = True
# if month is not december, end year is previous year
else:
  YEAR_END -= 1


# EVENT SITE INFO
EVENT_BASE_URL = "https://adventofcode.com/"
def get_input_url(year, day):
  url = "https://adventofcode.com/{year}/day/{day}/input"
  return url


# PROJECT FILE & FOLDER NAMES
SOLUTION_1_FILE = "solution_1.py"
SOLUTION_2_FILE = "solution_2.py"
INPUT_FILE = "input.txt"

