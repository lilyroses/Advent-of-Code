# show_progress_calendar.py
import json
import os
import sys


# Progress info
progress_file = "progress_data.json"
with open(progress_file, "r") as f:
  progress_data = json.load(f)

YEARS = progress_data.keys()
DAYS = [str(i) for i in range(1,26)]

TOTAL_PUZZLES = 0
SOLVED_PUZZLES = 0
for year in YEARS:
  for day in DAYS:
    TOTAL_PUZZLES += 2  # each day has 2 solutions
    SOLVED_PUZZLES += progress_data[year][day]
PERCENT_COMPLETE = (TOTAL_PUZZLES / SOLVED_PUZZLES) // 100
PERCENT_COMPLETE = f"{PERCENT_COMPLETE:.01f}%"

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
  days_row_border = f"{days_row_border:^{SCREEN_SIZE}}"
  return days_row_border

def build_day_progress_markers(lvl_solved):
  progress_markers = STAR * lvl_solved
  progress_narkers_square = f"{progress_markers:^{day_square_width}}"
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

  day_progress_row = ""
  day_border = build_day_row_border()

  day_blank_square = PIPE + (day_width*SPACE)
  day_blank_row = (day_blank_square * DAYS_PER_ROW) + PIPE
  day_blank_row = f"{day_blank_row:^{SCREEN_WIDTH}}"


  for day in range(day_start, day_end+1):
    day_progress_row = ""
    day = str(day)
    progress = PROGRESS_DATA[year][day]
    day_progress_markers = build_day_progress_narkers(progress)
    days_progress_row += day_progress_markers
  days_progress_row += PIPE
  days_progress_row = f"{days_progress_row:^{SCREEN_WIDTH}}"


calendar_border = build_horiz_border()
calendar_title_banner = build_calendar_title_banner()


calendar += year_title_banner
  

calendar = ""
calendar += calendar_border
calendar += calendar_title_banner
calendar += calendar_border

print(calendar)
