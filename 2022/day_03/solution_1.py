# Solution 1 - Advent of Code 2022, Day 3
from string import ascii_letters


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  letter_map = dict(zip(ascii_letters,
                        range(1, len(ascii_letters)+1)))
  total = 0
  for line in lines:
    n = len(line)
    s1 = set(sorted(line[:n//2]))
    s2 = set(sorted(line[n//2:]))
    c = list(s1 & s2)[0]
    total += letter_map[c]
  print(total)


if __name__ == "__main__":
  main()
