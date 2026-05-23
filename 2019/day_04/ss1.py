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

        while n != 0:
            d = n%10
            n = n//10
            if d == pd:
                has_pair = True
            if d <= pd:
                ds.append(d)
            else:
                return False
        return has_pair


    nums = []
    for i in range(x, y+1):
        if is_valid(i):
            nums.append(i)
    print(nums)


if __name__ == "__main__": main()
