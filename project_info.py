# project_info.py
from datetime import datetime


# EVENT DATE INFO
current = datetime.today()  # current date

DAY_START = 1
DAY_END = 25
YEAR_START = 2015
YEAR_END = current.year


def validate_progress_data(progress_data):

    def validate_year_keys(year_keys):
        error_msg = (
            f"ERROR: Year keys should be in ascending order from " \
            f"2015 - current year (or the previous year, if the " \
            f"current month is not December).\n"
        )

        if int(year_keys[0]) != START_YEAR:
            info = (
                f"\nInvalid start year key (year_keys[0]): {year_keys[0]} " \
                f"(should be {YEAR_START})\n"
            )
            print(f"{error_msg}{info}")
            return False

        if int(year_keys[-1]) != END_YEAR:
            info = (
                f"\nInvalid end year key (year_keys[-1]): {year_keys[-1]} " \
                f"(should be {YEAR_END})\n"
            )
            print(f"{error_msg}{info}")
            return False


        for year in enumerate(year_keys[:-1]):
            if int(year) >= int(year_keys[i+1]):
                info = (
                    f"\nInvalid range found: {year_keys[i]-" \
                    f"{year_keys[i+1]}\n" \
                    f"year_keys: {list(year_keys)}\n"
                )
                print(f"{error_msg}{info}")
                return False
        if int(year) != YEAR_START:
            print(error_msg)


# EVENT SITE INFO
BASE_URL = "https://adventofcode.com/"

def fmt_url(year_no, day_no):
    year_day_path = f"{year_no}/day/{day_no}/"
    url = BASE_URL + year_day_path
    return url


# PROJECT FILE & FOLDER NAMES
SOLUTION_1_FILE = "solution_1.py"
SOLUTION_2_FILE = "solution_2.py"
INPUT_FILE = "input.txt"

