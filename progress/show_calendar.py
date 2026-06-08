import json
import os
import sys


# EXTERN DATA REF
PROGRESS_DATA_FILE = "progress_data.json"
with open(PROGRESS_DATA_FILE, "r") as f:
    PROGRESS_DATA = json.load(f)


# ========================= SIZING & SYMBOLS =================================

# SYMBOLS FOR ASCII CALENDAR
CORNER  = '+'
DASH    = '-'
HZ_BOLD = '='
HZ_REG  = "_"
PIPE    = '|'
SPACE   = ' '
STAR    = '*'
DOT     = '.'

# SIZING
SCREEN_WIDTH = os.get_terminal_size()[0]
DAYS_PER_ROW = 5
# The number of PIPE chars to divide a row of days.
NUM_DIV_PER_ROW = (DAYS_PER_ROW + 1) * len(PIPE)
# for progress bars; 50 spaces for stars & extra for div chars, spaces, etc.
DAY_SQUARE_WIDTH = 10  # interior of cell; does not include PIPE chars
CALENDAR_WIDTH = (DAYS_PER_ROW * DAY_SQUARE_WIDTH) + NUM_DIV_PER_ROW
PROGRESS_BAR_WIDTH = CALENDAR_WIDTH - 6  # -6 to account for the surrounding chars, "| [" and " ] |"


if SCREEN_WIDTH < CALENDAR_WIDTH:
    print(f"\nError: Terminal width too small to display calendar. \
          Please resize and try again\n.")
    sys.exit()


# ================= CALENDAR TITLES ==========================================


def get_progress_bar(
        total_stars: int,
        stars_earned: int):
    """Creates a progress bar for the calendar title, like so:
    
| [ % PROGRESS BAR 50 / 500                    (10.0 %)] |
| [*****...............................................] |
    
    """
    percent_complete = (stars_earned / total_stars) * 100
    str_percent_complete = str(percent_complete)
    fmt_str_percent_complete = str_percent_complete[:str_percent_complete.index('.') + 2]
    stars_progress_bar = round((percent_complete // 2)) * STAR
    dots_progress_bar = (PROGRESS_BAR_WIDTH - len(stars_progress_bar)) * DOT

    pb_line_1_left = f"| [ % PROGRESS BAR - {stars_earned} / {total_stars}"
    pb_line_1_right = f"({fmt_str_percent_complete} %) ] |"
    pb_line_1_spaces = (CALENDAR_WIDTH - (len(pb_line_1_left) + len(pb_line_1_right))) * SPACE
    pb_line_1 = pb_line_1_left + pb_line_1_spaces + pb_line_1_right

    pb_line_2_left = "| ["
    pb_line_2_right = "] |"
    pb_line_2 = pb_line_2_left + stars_progress_bar + dots_progress_bar + pb_line_2_right

    progress_bar_lines = "\n".join([pb_line_1, pb_line_2])
    return progress_bar_lines


def get_title_banner():
    TITLE_BANNER_START = """
+======================================================+
|                                                      |
|           ___________________________________        |
|           A D V E N T      O F        C O D E        |
|           ___________________________________        |
|           ___________________________________        |
|           P R O G R E S S     C A L E N D A R        |
|           ___________________________________        |
|                                                      |
|                                                      |
+======================================================+
+------------------------------------------------------+
|                                                      |"""

    TITLE_BANNER_END = """|                                                      |
|______________________________________________________|
+======================================================+"""

    total_puzzles = sum(2 for _, days in PROGRESS_DATA.items() for _ in days)
    total_completed_puzzles = sum(score for _, days in PROGRESS_DATA.items()
                              for _, score in days.items())
    progress_bar = get_progress_bar(
        total_stars=total_puzzles,
        stars_earned=total_completed_puzzles)
    
    PROGRESS_BAR_LINES = "\n".join([TITLE_BANNER_START, progress_bar, TITLE_BANNER_END])
    return PROGRESS_BAR_LINES


def get_border_bold():
    dashes = HZ_BOLD * (CALENDAR_WIDTH-2)
    return CORNER + dashes + CORNER


def get_border():
    dashes = DASH * (CALENDAR_WIDTH-2)
    return CORNER + dashes + CORNER


def get_empty_line():
    spaces = SPACE * (CALENDAR_WIDTH-2)
    return PIPE + spaces + PIPE


def create_calendar(year):
    hz_border_bold = get_border_bold()
    hz_border = get_border()
    empty_line = get_empty_line()


    horiz_border_bold = CORNER + (HZ_BOLD*(CALENDAR_WIDTH-2)) + CORNER
    
    fmt_year = "[ " + " ".join(list(year)) + " ]"
    year_title_left_spaces = (CALENDAR_WIDTH - (len(fmt_year)+1) // 2) * SPACE
    year_title_right_spaces = (CALENDAR_WIDTH - (len(year_title_left_spaces)+1)) * SPACE
    year_title_line = PIPE + year_title_left_spaces + fmt_year + year_title_right_spaces + PIPE


# ==================== CREATE CALENDARS =========================
title_banner = get_title_banner()
print(title_banner)


ex4 = """
+======================================================+
|                                                      |
|                     [ 2 0 2 5 ]                      |
|                                                      |
+======================================================+
+------------------------------------------------------+
|                                                      |
| [ % PROGRESS BAR % ] :  37 / 50           [ 97.8 % ] |
| [***********************************...............] |
|______________________________________________________|
+----------+----------+----------+----------+----------+
|    01    |    02    |    03    |    04    |    05    |
|    **    |    **    |     *    |    **    |          |  
+----------+----------+----------+----------+----------+
|    06    |    07    |    08    |    09    |    10    |
|    **    |    **    |     *    |    **    |          |
+----------+----------+----------+----------+----------+
|    11    |    12    |    13    |    14    |    15    |
|    **    |    **    |     *    |    **    |          |  
+----------+----------+----------+----------+----------+
|    16    |    17    |    18    |    19    |    20    |  
|    **    |    **    |     *    |    **    |          |  
+----------+----------+----------+----------+----------+
|    21    |    22    |    23    |    24    |    25    |  
|    **    |    **    |     *    |    **    |          |  
+----------+----------+----------+----------+----------+
"""
