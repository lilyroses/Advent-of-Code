# Solution 1 - Advent of Code 2017, Day 2

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    spreadsheet = []
    for line in lines:
        row = [int(num) for num in line.split()]
        spreadsheet.append(row)

    total = 0
    for row in spreadsheet:
        total += max(row) - min(row)

    print(total)


if __name__ == "__main__":
    main()
