# Solution 2 - Advent of Code 2016, Day 4
from string import ascii_lowercase as letters


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    LETTERS = list(letters)
    NUMS = list(range(0, len(LETTERS)))
    LETTER_MAP = dict(zip(LETTERS, NUMS))
    MAP_LETTER = dict(zip(NUMS, LETTERS))

    for line in lines:
        room_id = line.split("-")
        s = "-".join(room_id[:-1])
        sector_id = int(room_id[-1].split("[")[0])

        new_letters = ""
    
        for char in s:
            if char not in LETTERS:
                new_letters += char
            else:
                original_val = LETTER_MAP[char]
                new_val = (original_val + sector_id) % len(LETTERS)
                new_char = MAP_LETTER[new_val]
                new_letters += new_char
        if "north" in new_letters:
            print(new_letters, sector_id)
    


if __name__ == "__main__":
    main()
