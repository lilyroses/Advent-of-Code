# Solution 2 - Advent of Code 2021, Day 1
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    vals = [int(line) for line in lines]

    sums = []
    total = 0
    for i in range(len(vals)-2):
        j = i + 1
        k = i + 2
        s = vals[i] + vals[j] + vals[k]
        if not sums:
            sums.append(s)
        else:
            diff = s - sums[-1]
            if diff > 0:
                total += 1
            sums.append(s)
    print(total)
    print(vals[k], vals[-1])


if __name__ == "__main__":
    main()
