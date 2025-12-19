# build_calendar.py
import os
import sys
from datetime import datetime
from event_info import YEARS


# EVENT INFO
current_month = datetime.today().month
current_year = datetime.today().year
if current_month == 12 and current_year not in YEARS:
    print("\nError: Please update `event_info.py` to reflect the current \
          year's event info.\n")
    sys.exit()

# CALENDAR SYMBOLS AND SIZES
CORNER = "+"
DASH = "-"
PIPE = "|"
SPACE = " "
STAR = "*"

# SCREEN WIDTH, CALENDAR DAY AND WEEK WIDTHS
SCREEN_WIDTH = os.get_terminal_size()[0]
DAYS_PER_ROW = 5
MIN_DAY_WIDTH = 4  # does not include pipe chars


def get_day_width(SCREEN_WIDTH, MIN_DAY_WIDTH=4, DAYS_PER_ROW=5):
    # final len(PIPE) is to account for final pipe char that closes calendar
    # row
    MIN_CALENDAR_WIDTH = (MIN_DAY_WIDTH * DAYS_PER_ROW)
    + (len(PIPE) * DAYS_PER_ROW) + len(PIPE)
    if SCREEN_WIDTH < MIN_CALENDAR_WIDTH:
        print("Error: screen width too small to display calendar.")
        sys.exit()

    if SCREEN_WIDTH >= MIN_CALENDAR_WIDTH:
        extra_spaces = SCREEN_WIDTH - MIN_CALENDAR_WIDTH
        extra_day_spaces = extra_spaces // DAYS_PER_ROW
        day_width = MIN_DAY_WIDTH + extra_day_spaces

    return day_width


day_width = get_day_width(SCREEN_WIDTH, MIN_DAY_WIDTH, DAYS_PER_ROW)


def create_calendar_line(days_per_row, day_items, day_width):
    if not day_items:
        day_items = ["" for day in range(days_per_row)]
    if len(day_items) != days_per_row:
        print(f"\nError: number of day items must match days per row.\n")
        sys.exit()

    calendar_line = ""
    for item in day_items:
        item = str(item)
        cell_spaces = day_width - len(item)
        left_spaces = (cell_spaces // 2) * SPACE
        right_spaces = (day_width - left_spaces) * SPACE
        cell_interior = PIPE + left_spaces + item + right_spaces
        calendar_line += cell_interior
    calendar_line += PIPE
    return calendar_line


def create_dates_line(day_start: int, day_end: int, day_width: int) -> str:
    """Create the part of the calendar's week row which holds the date.
    
    ex:
    date_line = |   1   |   2   |   3   |   4   |   5   |

    """
    row_str = ""
    for day in range(day_start, day_end+1):
        day_str = str(day)
        day_width = day_width - len(day_str)
        left_spaces = day_width // 2
        right_spaces = day_width - left_spaces
        day_cell = (PIPE + (SPACE * left_spaces)
                    + day_str + (SPACE * right_spaces))
        row_str += day_cell
    row_str += PIPE
    return row_str


row = create_dates_line(6, 10, day_width)
print(row)
