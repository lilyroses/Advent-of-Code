# Solution 2 - Advent of Code 2017, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    """Solution 2"""
    captcha = lines[0]
    total = 0
  
    x = len(captcha)
    steps = x // 2

    for i in range(x):
        j = i + steps
        if j > x - 1:
            j = abs(x - j)
        num1 = captcha[i]
        num2 = captcha[j]
        if num1 == num2:
            print(i, j)
            total += int(num1)

    print(total)


if __name__ == "__main__":
    main()
