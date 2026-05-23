# Solution 1 - Advent of Code 2019, Day 4

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    x, y = [int(v) for v in lines[0].split('-')]


    def is_valid(n):
        has_pair = False
        pd = n%10
        n = n//10
        ds = [pd]

        while n > 0:
            d = n%10
            n = n//10
            if d == pd:
                has_pair = True
            if d <= pd:
                ds.append(d)
                pd = d
            else:
                return False
        return has_pair


    t = 0
    for i in range(x, y+1):
        if is_valid(i):
            t += 1
    print(t)


if __name__ == "__main__": main()
