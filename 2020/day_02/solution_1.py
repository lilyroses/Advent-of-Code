# Solution 1 - Advent of Code 2020, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    total = 0
    for line in lines:
        items = line.split()
        min_count, max_count = [int(i) for i in items[0].split('-')]
        char = items[1][:-1]
        pwd = items[-1]
        count = pwd.count(char)
        if count in range(min_count, max_count+1):
            total += 1
    print(total)


if __name__ == "__main__":
    main()
