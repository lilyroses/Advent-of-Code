# build_calendar.py
import os
import sys
from datetime import datetime


CORMER	= "+"
DASH	= "-"
PIPE	= "|"
SPACE	= " "
STAR 	= "*"

# CALENDAR DATES
current = datetime.today()

DAYS_PER_ROW	= 5
ROWS_PER_MONTH	= 5
DAYS_PER_MONTH	= DAYS_PER_ROW * ROWS_PER_MONTH
DAYS = list(range(1, DAYS_PER_MONTH+1))

YEAR_START	= 2016
YEAR_END 	= current.year
if current.month != 12:
  YEAR_END -= 1
YEARS = list(range(YEAR_START, YEAR_END+1))


# TERMINAL INFO
SCREEN_WIDTH = os.get_terminal_size()[0]

MIN_DAY_WIDTH = 5 #includes len of pipe char
MIN_CAL_WIDTH = (MIN_DAY_WIDTH * DAYS_PER_ROW) + 1  # +1 to account for final pipe char



def get_day_width(DAYS_PER_ROW, SCREEN_WIDTH):
  if SCREEN_WIDTH < MIN_CAL_WIDTH:
    print("Error: screen width too small to display calendar.")
    sys.exit()

  if SCREEN_WIDTH >= MIN_CAL_WIDTH:
    extra_spaces = SCREEN_WIDTH - MIN_CAL_WIDTH
    extra_day_spaces = extra_spaces // DAYS_PER_ROW
    day_width = MIN_DAY_WIDTH + extra_day_spaces

  return day_width


def get_calendar_width(DAYS_PER_ROW):
  day_width = get_day_width(DWYS_PER
calendar_width = (DAYS_PER_ROW * day_width) + 1  # +1 is for final PIPE char


