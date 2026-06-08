# Solution 1 - Advent of Code 2020, Day 1
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    vals = [int(line) for line in lines]
    for i in range(len(vals[:-1])):
        for j in range(i+1, len(vals)):
            x = vals[i]
            y = vals[j]
            if x+y == 2020:
                print(x*y)


if __name__ == "__main__":
    main()
