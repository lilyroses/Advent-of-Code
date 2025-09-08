# Solution 1 - Advent of Code 2016, Day 4
from collections import defaultdict as dd
from itertools import groupby


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():

    total = 0

    for line in lines:
        room_id = line.split("-")
        name = "".join(room_id[:-1])
        sector_id = int(room_id[-1].split("[")[0])
        checksum = room_id[-1].split("[")[1][:-1]
        
        letter_groups = sorted([''.join(g) for _, g in groupby(sorted(name))], reverse=True, key=len)

        check = ""
        for s in letter_groups[:5]:
            c = s[0]
            check += c

        if check == checksum:
            total += sector_id

    print(total)


if __name__ == "__main__":
    main()
