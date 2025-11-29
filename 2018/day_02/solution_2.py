# Solution 2 - Advent of Code 2018, Day 2
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  t = 0

  for i in range(len(lines)-1):
    w = lines[i]
    for j in range(i+1, len(lines)):
      w2 = lines[j]
      d = 0
      for x in range(len(w)):
        char = w[x]
        char2 = w2[x]
        if char != char2:
          d += 1
          y = x
      if d == 1:
        print(w[:y]+w[y+1:])


if __name__ == "__main__":
  main()
