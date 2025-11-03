# show_progress_calendar.py
import json
import os
import sys


# Progress info
PROGRESS_FILE = "progress_data.json"
with open(PROGRESS_FILE, "r") as f:
  PROGRESS_DATA = json.load(f)

YEARS = PROGRESS_DATA.keys()
DAYS = [str(i) for i in range(1,26)]

TOTAL_PUZZLES = 0
SOLVED_PUZZLES = 0
for year in YEARS:
  for day in DAYS:
    TOTAL_PUZZLES += 2  # each day has 2 solutions
    SOLVED_PUZZLES += PROGRESS_DATA[year][day]
PERCENT_COMPLETE = (SOLVED_PUZZLES*100) / TOTAL_PUZZLES
PERCENT_COMPLETE = f"{PERCENT_COMPLETE:.2f}%"

# Calendar characters
SPACE = " "
DASH = "-"
PIPE = "|"
CORNER = "+"
STAR = "*"

# Calendar size
DAYS_PER_EVENT = 25
DAYS_PER_ROW = 5
CORNERS_PER_ROW = DAYS_PER_ROW + 1

min_day_square_width = 5  # interior cell width
min_calendar_width = (min_day_square_width * DAYS_PER_ROW) + CORNERS_PER_ROW
# If screen is too small
SCREEN_WIDTH = os.get_terminal_size()[0]
if SCREEN_WIDTH < min_calendar_width:
  print("\nError: Screen width too small to display calendar.")
  sys.exit()
# If screen is larger than or equal to minimum
# calendar size requirement
if SCREEN_WIDTH >= min_calendar_width:
  extra_spaces = SCREEN_WIDTH - min_calendar_width
  extra_day_spaces = extra_spaces // DAYS_PER_ROW
  day_square_width = min_day_square_width + extra_day_spaces

calendar_width = (day_square_width * DAYS_PER_ROW) + CORNERS_PER_ROW

# Calendar borders
title_border = CORNER + ((calendar_width-2)*DASH) + CORNER
day_square_border = CORNER + (day_square_width * DASH)
day_row_border = (day_square_border * DAYS_PER_ROW) + CORNER

# Calendar rows
empty_day = PIPE + (day_square_width * SPACE)
empty_row = PIPE + ((calendar_width-2)*SPACE) + PIPE


# Calendar components
def build_blank_line():
  blank_line = SPACE * SCREEN_WIDTH
  return blank_line

def build_empty_row():
  empty_row = PIPE + ((calendar_width-2) * SPACE) + PIPE
  empty_row = f"{empty_row:^{SCREEN_WIDTH}}"
  return empty_row

def build_horiz_border():
  horiz_border = CORNER + ((calendar_width-2) * DASH) + CORNER
  horiz_border = f"{horiz_border:^{SCREEN_WIDTH}}"
  return horiz_border


def build_calendar_title_banner():
  title_1 = "ADVENT OF CODE PROGRESS"
  title_1 = f"{title_1:^{calendar_width-2}}"
  title_1 = PIPE + title_1 + PIPE

  title_2 = "CALENDAR"
  title_2 = f"{title_2:^{calendar_width-2}}"
  title_2 = PIPE + title_2 + PIPE
  title_2 = f"{title_2:^{SCREEN_WIDTH}}"

  title_3 = f"total: {SOLVED_PUZZLES}/{TOTAL_PUZZLES} ({PERCENT_COMPLETE})"
  title_3 = f"{title_3:^{calendar_width-2}}"
  title_3 = PIPE + title_3 + PIPE
  title_3 = f"{title_3:^{SCREEN_WIDTH}}"

  calendar_title_banner = f"""{title_1:^{SCREEN_WIDTH}}
{title_2:^{SCREEN_WIDTH}}
{empty_row:^{SCREEN_WIDTH}}
{title_3:^{SCREEN_WIDTH}}"""
  return calendar_title_banner


def build_year_title_banner(year):
  year_title_banner = f"{year:^{calendar_width-2}}"
  year_title_banner = PIPE + year_title_banner + PIPE
  year_title_banner = f"{year_title_banner:^{SCREEN_WIDTH}}"
  return year_title_banner


def build_days_row_border():
  day_border = CORNER + (day_square_width * DASH)
  days_row_border = (day_border * DAYS_PER_ROW) + CORNER
  days_row_border = f"{days_row_border:^{SCREEN_WIDTH}}"
  return days_row_border

def build_day_progress_markers(lvl_solved):
  progress_markers = STAR * lvl_solved
  progress_markers_square = f"{progress_markers:^{day_square_width}}"
  progress_markers_square = PIPE + progress_markers_square
  return progress_markers_square

def empty_day_square():
  empty_day_square = PIPE + (SPACE * day_square_width)
  empty_day_square = f"{empty_day_square:^{SCREEN_WIDTH}}"
  return empty_day_square

def day_square_num(day):
  day_square_num = f"{day:^{day_square_width}}"
  day_square_num = PIPE + day_square_num
  day_square_num = f"{day_square_num:^{SCREEN_WIDTH}}"
  return day_square_num


def build_day_row(year, day_start, day_end):
  days_border = build_days_row_border()

  days_progress_row = ""
  days_num_row = ""

  for day in range(day_start, day_end+1):
    progress = PROGRESS_DATA[str(year)][str(day)]
    days_progress_markers = build_day_progress_markers(progress)
    days_progress_row += days_progress_markers
    day_num_square = f"{day:^{day_square_width}}"
    day_num_square = PIPE + day_num_square
    days_num_row += day_num_square
  days_progress_row += PIPE
  days_progress_row = f"{days_progress_row:^{SCREEN_WIDTH}}"
  days_num_row += PIPE

  day_blank_square = PIPE + (day_square_width*SPACE)
  days_blank_row = (day_blank_square * DAYS_PER_ROW) + PIPE

  day_row = f"""
{days_border:^{SCREEN_WIDTH}}
{days_blank_row:^{SCREEN_WIDTH}}
{days_progress_row:^{SCREEN_WIDTH}}
{days_blank_row:^{SCREEN_WIDTH}}
{days_num_row:^{SCREEN_WIDTH}}
{days_blank_row:^{SCREEN_WIDTH}}"""
  return day_row


calendar = ""
blank_line = build_blank_line()
calendar_border = build_horiz_border()
empty_row = build_empty_row()
calendar_title_banner = build_calendar_title_banner()
days_row_border = build_days_row_border()

calendar += calendar_border
calendar += empty_row
calendar += calendar_title_banner
calendar += empty_row
calendar += calendar_border
calendar += blank_line

for year in YEARS:
  calendar += calendar_border
  calendar += empty_row
  calendar += build_year_title_banner(year)
  calendar += empty_row
  calendar += build_day_row(year, 1, 5)
  calendar += build_day_row(year, 6, 10)
  calendar += build_day_row(year, 11, 15)
  calendar += build_day_row(year, 16, 20)
  calendar += build_day_row(year, 21, 25)
  calendar += days_row_border
  calendar += blank_line

print(calendar)
