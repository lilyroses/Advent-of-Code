# Solution 1 - Advent of Code 2021, Day 1
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    vals = [int(line) for line in lines]

    total = 0
    for i in range(len(vals)-1):
        j = i + 1
        diff = vals[j] - vals[i]
        if diff > 0:
            total += 1
    print(total)

    print("\n\n", vals[j], vals[-1])


if __name__ == "__main__":
    main()
