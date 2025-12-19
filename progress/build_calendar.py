# build_calendar.py
import os
import sys
from datetime import datetime
from event_info import EVENT_YEAR_DAYS, YEARS, PUZZLES_PER_DAY


# EVENT INFO
current_month = datetime.today().month
current_year = datetime.today().year
if current_month == 12 and current_year not in EVENT_YEAR_DAYS:
  print("\nError: Please update `event_info.py` to reflect the current year's event info.\n")
  sys.exit()

# CALENDAR SYMBOLS AND SIZES
CORNER	= "+"
DASH	= "-"
PIPE	= "|"
SPACE	= " "
STAR 	= "*"

# SCREEN WIDTH, CALENDAR DAY AND WEEK WIDTHS
SCREEN_WIDTH = os.get_terminal_size()[0]
DAYS_PER_ROW  = 5
MIN_DAY_WIDTH = 4 # does not include pipe chars


def get_day_width(SCREEN_WIDTH, MIN_DAY_WIDTH=4, DAYS_PER_ROW=5):
  MIN_CALENDAR_WIDTH = (MIN_DAY_WIDTH * DAYS_PER_ROW) + (len(PIPE) * DAYS_PER_ROW) + len(PIPE) # final len(PIPE) is to account for final pipe char that closes calendar row

  if SCREEN_WIDTH < MIN_CALENDAR_WIDTH:
    print("Error: screen width too small to display calendar.")
    sys.exit()

  if SCREEN_WIDTH >= MIN_CALENDAR_WIDTH:
    extra_spaces = SCREEN_WIDTH - MIN_CALENDAR_WIDTH
    extra_day_spaces = extra_spaces // DAYS_PER_ROW
    day_width = MIN_DAY_WIDTH + extra_day_spaces

  return day_width


day_width = get_day_width(DAYS_PER_ROW, SCREEN_WIDTH
