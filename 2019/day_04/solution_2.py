# Solution 2 - Advent of Code 2019, Day 4
from collections import defaultdict


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    x, y = [int(v) for v in lines[0].split('-')]

    def is_valid(n):
        pd = n%10
        n = n//10
        ds_map = defaultdict(int)
        ds_map[pd] += 1

        while n != 0:
            d = n%10
            if d > pd:
                return False
            n = n//10
            ds_map[d] += 1
            pd = d
        return 2 in ds_map.values()


    t = 0
    for i in range(x, y+1):
        if is_valid(i):
            t += 1
    print(t)


if __name__ == "__main__":
    main()
