import json
import sys


def update_progress(year, day, score):

    VALID_SCORES = (0,1,2)
    if score not in VALID_SCORES:
        print(f"\nError: Invalid score [{score}]. Valid score values are:\n{VALID_SCORES}\n")
        sys.exit()

    PROGRESS_DATA_FILE = "progress_data.json"
    with open(PROGRESS_DATA_FILE, "r") as f:
        PROGRESS_DATA = json.load(f)
    
    YEAR_KEYS = list(PROGRESS_DATA.keys())
    if year not in YEAR_KEYS:
        print(f"\nError: Invalid year. Valid year keys are:\n{YEAR_KEYS}\n")
        sys.exit()

    DAY_KEYS = list(PROGRESS_DATA[year].keys())
    if day not in DAY_KEYS:
        print(f"\nError: Invalid day for year {year}. Valid day keys are:\n{DAY_KEYS}\n")
        sys.exit()

    cur_score = PROGRESS_DATA[year][day]
    if cur_score == score:
        sys.exit()
    if cur_score > score:
        print(f"\nScore for {year}, Day {day} is already listed as [{cur_score}].")
        while True:
            revert = input("Revert score? (y/n): ")
            if revert.lower() == 'n':
                print("\nOperation cancelled.\nExiting...\n")
                sys.exit()
            elif revert.lower() == 'y':
                break
    
    PROGRESS_DATA[year][day] = score
    with open(PROGRESS_DATA_FILE, "w") as f:
        json.dump(PROGRESS_DATA, f)

    print(f"\nSuccessfully updated score for {year}, Day {day}: [{score}]\n")
    sys.exit()


if __name__ == "__main__":
    args = sys.argv[1:]

    year, day, score = sys.argv[1:]
    score = int(score)
    update_progress(year, day, score)

