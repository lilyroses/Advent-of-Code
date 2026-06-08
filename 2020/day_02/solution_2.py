# Solution 2 - Advent of Code 2020, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    total = 0
    for line in lines:
        valid_spots = 0
        items = line.split()
        idx1, idx2 = [int(i) for i in items[0].split('-')]
        char = items[1][:-1]
        pwd = items[-1]
        if pwd[idx1-1] == char:
            valid_spots += 1
        if pwd[idx2-1] == char:
            valid_spots += 1
        if valid_spots == 1:
            total += 1
    print(total)    


if __name__ == "__main__":
    main()
