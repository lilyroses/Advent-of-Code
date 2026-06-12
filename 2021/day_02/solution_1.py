# Solution 1 - Advent of Code 2021, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    x, y = 0, 0
    for line in lines:
        dir, val = line.split()
        val = int(val)
        if dir == "forward":
            x += val
        elif dir == "up":
            y -= val
        elif dir == "down":
            y += val
        else:
            print(f"Unknown direction '{dir}'")
    ans = x * y
    print(ans)


if __name__ == "__main__":
    main()
