# Solution 1 - Advent of Code 2017, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    captcha = lines[0]
    total = 0
    for i in range(len(captcha)):
        if i == len(captcha)-1:
            j = 0
        else:
            j = i + 1
        n = captcha[i]
        m = captcha[j]
        if n == m:
            total += int(n)

    print(total)

if __name__ == "__main__":
    main()
