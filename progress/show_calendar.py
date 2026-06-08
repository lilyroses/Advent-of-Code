import json
import os
import sys


# =========================== CONSTANTS ===============================

# ---------------- EXTERN DATA REF ------------------------------------
PROGRESS_DATA_FILE = "progress_data.json"
with open(PROGRESS_DATA_FILE, "r") as f:
    PROGRESS_DATA = json.load(f)


def get_total_puzzles_all():
    """Returns the sum total of all possible earned stars for each
    Advent of Code event."""
    total_puzzles = sum(2 for _, days in PROGRESS_DATA.items()
                        for _ in days)
    return total_puzzles


def get_total_puzzles_completed():
    """Returns the sum total of stars earned for all Advent of Code
    events."""
    total_completed_puzzles = sum(score for _, days in PROGRESS_DATA.items()
                              for _, score in days.items())
    return total_completed_puzzles


def get_total_puzzles_year(year):
    """Returns the total number of stars that can be earned for this
    year's Advent of Code event."""

    total_puzzles = sum(2 for _ in PROGRESS_DATA[year].keys())
    return total_puzzles


def get_puzzles_completed_year(year):
    """Returns the total number of stars that have been earned for this
    year's Advent of Code event."""
    total_completed_puzzles = sum(score for _, score in PROGRESS_DATA[year].items())
    return total_completed_puzzles


# ----------------------------- SYMBOLS -------------------------------
CORNER  = '+'
DASH    = '-'
HZ_BOLD = '='
HZ_REG  = "_"
DIV     = '|'
SPACE   = ' '
STAR    = '*'
DOT     = '.'

# ----------------------------- SIZING --------------------------------
SCREEN_WIDTH = os.get_terminal_size()[0]
DAYS_PER_ROW = 5
DAY_SQUARE_WIDTH = 10  # interior of cell; does not include DIV chars
# The number of DIV chars to divide a row of days.
NUM_DIV_PER_ROW = (DAYS_PER_ROW + 1) * len(DIV)
CALENDAR_WIDTH = (DAYS_PER_ROW * DAY_SQUARE_WIDTH) + NUM_DIV_PER_ROW
# -6 to account for the surrounding chars, "| [" and " ] |"
PROGRESS_BAR_WIDTH = CALENDAR_WIDTH - 6
                               
if SCREEN_WIDTH < CALENDAR_WIDTH:
    print(f"\nError: Terminal width too small to display calendar. " \
          "Please resize and try again\n.")
    sys.exit()


# ======================= CALENDAR ====================================

# -------------- LINES ------------------------------------------------
def get_border(bold=False):
    """Gets a horizontal border of DASH characters that runs the length
    of the calendar, beginning with CORNER chars on the left and right.
    Used for banner borders.
    
    Example:
    +-----------------------------------------------------+
    """
    num_dashes = CALENDAR_WIDTH - 2
    dash = DASH
    if bold==True:
        dash = HZ_BOLD
    dashes = dash * num_dashes
    border = CORNER + dashes + CORNER
    return border


def get_week_border():
    """Gets a horizontal border of dashes that also has CORNER chars to
    delimit each day square.
    
    Example:
    
    +----------+----------+----------+----------+----------+
    """
    day_border = CORNER + (DASH * DAY_SQUARE_WIDTH)
    week_border = (day_border * DAYS_PER_ROW) + DIV
    return week_border


def get_empty_row():
    """Gets an empty row for the entire calendar with. Produces a line
    of blank spaces with a DIV char on the left and right.
    
    Example:
    |                                                     |
    """
    num_spaces = CALENDAR_WIDTH - 2
    spaces = SPACE * num_spaces
    empty_row = DIV + spaces + DIV
    return empty_row


def get_week_empty_row():
    """Gets an empty row for a calendar week. Produces a divider for
    each day and the requisite number of spaces between each to create
    a week of days that are of size DAY_SQUARE_WIDTH.
    
    Example:
    |          |          |          |          |          |
    """
    week_empty_row = ""
    for i in range(DAYS_PER_ROW):
        week_empty_row += DIV + (SPACE * DAY_SQUARE_WIDTH)
    week_empty_row += DIV
    return week_empty_row


def get_underline(text):
    """Get a line of underline characters that is centered underneath
    some text (the function argument). Does not include left/right
    spacing or DIV chars on the right and left (use
    fmt_title_line(text) to do so).

    Example:
    A D V E N T   O F   C O D E    <---- Example 'text' string arg
    ___________________________    <---- Produced underline.
    """
    num_hz_reg = len(text)
    underline = HZ_REG * num_hz_reg
    return underline


def fmt_title_line(text):
    """Places a title line in between divider characters with spacing
    around either side of the text to center the text in the middle of
    a line that is the width of the CALENDAR_WIDTH.
    
    Example:
    |                     [ 2 0 2 3 ]                      |
    """
    num_spaces = (CALENDAR_WIDTH - 2) - len(text)
    left_spaces = (num_spaces // 2) * SPACE
    right_spaces = (num_spaces - len(left_spaces)) * SPACE
    title = DIV + left_spaces + text + right_spaces + DIV
    return title


def fmt_year_title_str(year):
    """Formats a year title line for a calendar year banner.
    First, formats a year title string like so:
        year_str = [ 2 0 2 5 ]
    Next, calls the fmt_title_line() function passing year_str as the
    only argument. Produces a centered, formatted year title line with
    a width of CALENDAR_WIDTH and beginning and ending with DIV
    characters.
    
    Example:
    |                     [ 2 0 2 3 ]                      |
    """
    year_str = list(str(year))
    fmt_year = "[ " + " ".join(year_str) + " ]"
    year_title_line = fmt_title_line(fmt_year)
    return year_title_line


def fmt_week_days_line(day_start, day_end):
    """Shows the day number line for a calendar week row.
    When preceded with a calednar week row border and followed by a
    blank row or a progress star line and closed with another week row
    border, forms an entire ASCII calendar week.

    Example:
    
    |    1     |    2     |    3     |    4     |    5     |
    
    """
    week_days_line = ""
    for day in range(day_start, day_end+1):
        day = str(day)
        num_day_square_spaces = DAY_SQUARE_WIDTH - len(day)
        num_day_square_spaces_left = num_day_square_spaces // 2
        num_day_square_spaces_right = num_day_square_spaces - num_day_square_spaces_left
        spaces_left = SPACE * num_day_square_spaces_left
        spaces_right = SPACE * num_day_square_spaces_right
        day_square = DIV + spaces_left + day + spaces_right
        week_days_line += day_square
    week_days_line += DIV
    return week_days_line


def fmt_week_progress_line(day_start, day_end, year):
    pass


# --------------------- BANNERS ---------------------------------------
def get_title_banner():
    """
    THIS IS SPECIFIC FOR THIS ADVENT OF CODE CALENDAR

    Title banner for the entire progress calendar. Shows a title
    banner and a progress bar for the percentage of total completed
    stars out of total possible stars for all year events.
    Example:
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
    +======================================================+"""
    title_text_1 = "A D V E N T      O F        C O D E"
    title_text_2 = "P R O G R E S S     C A L E N D A R"
    underline = get_underline(title_text_1)    

    border_bold = get_border(bold=True)
    empty_row = get_empty_row()

    fmt_title_text_1 = fmt_title_line(title_text_1)
    fmt_title_text_2 = fmt_title_line(title_text_2)
    fmt_underline = fmt_title_line(underline)

    title_banner_rows = [
        border_bold,
        empty_row,
        fmt_underline,
        fmt_title_text_1,
        fmt_underline,
        fmt_underline,
        fmt_title_text_2,
        fmt_underline,
        empty_row,
        border_bold,
    ]
    title_banner = "\n".join(title_banner_rows)
    return title_banner


def get_year_banner(year):
    """Example:
    +======================================================+
    |                                                      |
    |                     [ 2 0 2 5 ]                      |
    |                                                      |
    +======================================================+"""
    border_bold = get_border(bold=True)
    empty_row = get_empty_row()
    year_title = fmt_year_title_str(year)
    year_banner_rows = [
        border_bold,
        empty_row,
        year_title,
        empty_row,
        border_bold,
    ]
    year_banner = "\n".join(year_banner_rows)
    return year_banner
    

# ----------------- PROGRESS BAR --------------------------------------
def get_progress_bar(stars_earned, total_stars):
    """Example:
    +------------------------------------------------------+
    |                                                      |
    | [ % PROGRESS BAR % ] :  37 / 50           [ 97.8 % ] |
    | [***********************************...............] |
    |______________________________________________________|"""

    percent_complete = (stars_earned / total_stars) * 100
    str_percent_complete = str(percent_complete)
    fmt_str_percent_complete = str_percent_complete[:str_percent_complete.index('.') + 2]
    # the stars that indicate how full the progress bar is
    stars_progress_bar = round((percent_complete // 2)) * STAR
    # the dots that indicate the empty portion of the progress bar
    dots_progress_bar = (PROGRESS_BAR_WIDTH - len(stars_progress_bar)) * DOT

    pb_line_1_left = f"| [ % PROGRESS BAR % ] : {stars_earned} / {total_stars}"
    pb_line_1_right = f"[ {fmt_str_percent_complete} % ] |"
    pb_line_1_spaces = (CALENDAR_WIDTH - (len(pb_line_1_left) + len(pb_line_1_right))) * SPACE
    pb_line_1 = pb_line_1_left + pb_line_1_spaces + pb_line_1_right
    pb_line_2 = "| [" + stars_progress_bar + dots_progress_bar + "] |"

    border = get_border()
    empty_row = get_empty_row()
    # last row of banner; lower border of progress bar. see docstring.
    underline = get_underline(SPACE * (CALENDAR_WIDTH-2))
    underline = DIV + underline + DIV

    progress_bar_rows = [
        border,
        empty_row,
        pb_line_1,
        pb_line_2,
        underline
    ]

    progress_bar = "\n".join(progress_bar_rows)
    return progress_bar


# ----------------- CALENDAR WEEKS ------------------------------------
def get_calendar_week(year, day_start, day_end, PROGRESS_DATA):
    week_border = get_week_border()
    week_empty_row = get_week_empty_row()

    day_line = ""
    empty_line = ""


def get_calendar(year):
    week_border = get_week_border()
    pass



# CREATING THE CALENDARS
if __name__ == "__main__":

    total_stars = get_total_puzzles_all()
    stars_earned = get_total_puzzles_completed()
    title_banner = get_title_banner()
    progress_bar = get_progress_bar(stars_earned, total_stars)
    print(title_banner)
    print(progress_bar)
    print("\n\n")

    for year in PROGRESS_DATA.keys():
        total_stars = get_total_puzzles_year(year)
        stars_earned = get_puzzles_completed_year(year)
        year_banner = get_year_banner(year)
        progress_bar = get_progress_bar(stars_earned, total_stars)        
        print(year_banner)
        print(progress_bar)
        print("\n\n")

    week_days_line = fmt_week_days_line(1, 5)
    print(week_days_line)
