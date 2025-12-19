# Solution 2 - Advent of Code 2017, Day 4

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    total = 0
    for line in lines:
        passwords = line.split()
        passwords_sorted = ["".join(sorted(pwd)) for pwd in passwords]
        if len(set(passwords_sorted)) == len(passwords):
          total += 1

    print(total)


if __name__ == "__main__":
    main()
