# build_calendar.py
import os
from datetime import datetime


CORMER	= "+"
DASH	= "-"
PIPE	= "|"
SPACE	= " "
STAR 	= "*"

# CALENDAR DATES
DAYS_PER_ROW	= 5
ROWS_PER_MONTH	= 5
DAYS_PER_MONTH	= DAYS_PER_ROW * ROWS_PER_MONTH
DAYS = list(range(1, DAYS_PER_MONTH+1))

current = datetime.today()

YEAR_START	= 2016
YEAR_END 	= current.year
if current.month != 12:
  YEAR_END -= 1
YEARS = list(range(YEAR_START, YEAR_END+1))


min_day_width = 4  # not including_pipe_chars
min_row_width = (min_day_width * DAYS_PER_ROW) + (len(PIPE) * DAYS_PER_ROW) + len(PIPE)



