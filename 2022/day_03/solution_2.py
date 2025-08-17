# Solution 2 - Advent of Code 2022, Day 3
from string import ascii_letters


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  letter_map = dict(zip(ascii_letters,
                        range(1, len(ascii_letters)+1)))
  total = 0
  for i in range(0, len(lines), 3):
    substrs = lines[i:i+3]
    s = [set(substr) for substr in substrs]
    c = list(s[0] & s[1] & s[2])[0]
    total += letter_map[c]
  print(total)


if __name__ == "__main__":
  main()
