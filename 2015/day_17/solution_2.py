# Solution 2 - Advent of Code 2015, Day 17
from itertools import combinations


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  x = 0
  total = 150
  containers = [int(n) for n in lines]
  n = len(containers)

  combos = list(combinations(containers, 4))
  for combo in combos:
    if sum(combo) == total:
      x += 1

  print(x)


if __name__ == "__main__":
  main()
