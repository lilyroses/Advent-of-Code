# Solution 2 - Advent of Code 2019, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    vals = [int(n) for n in lines]

    def eval(v):
        t = 0
        while True:
            x = v // 3 - 2
            if x <= 0:
                return t
            t += x
            v = x

    totals = []
    for val in vals:
        totals.append(eval(val))
    print(sum(totals))


if __name__ == "__main__":
    main()
