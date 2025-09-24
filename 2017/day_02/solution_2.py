# Solution 2 - Advent of Code 2017, Day 2

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
        row = sorted(row)
        for i in range(len(row)-2):
            for j in range(i+1, len(row)-1):
                num1 = row[i]
                num2 = row[j]
                if num2 % num1 == 0:
                    total += num2 // num1

    print(total)


if __name__ == "__main__":
    main()
