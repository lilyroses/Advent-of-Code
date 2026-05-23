# Solution 1 - Advent of Code 2019, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    vals = [int(n) for n in lines]
    fuel_vals = sum([(v//3) - 2 for v in vals])
    print(fuel_vals)


if __name__ == "__main__":
    main()
