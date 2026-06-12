# Solution 2 - Advent of Code 2021, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    hz_pos = 0
    depth = 0
    aim = 0
    for line in lines:
        dir, val = line.split()
        val = int(val)
        if dir == "forward":
            hz_pos += val
            depth += (aim * val) 
        elif dir == "up":
            aim -= val
        elif dir == "down":
            aim += val
        else:
            print(f"Unknown direction '{dir}'")
    ans = hz_pos * depth
    print(ans)


if __name__ == "__main__":
    main()
