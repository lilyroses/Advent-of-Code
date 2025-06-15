# Solution 1 - Advent of Code 2015, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  lvl = {"(": 1, ")": -1}
  chars = list(lines[0])
  floor = 0
  for char in chars:
    floor += lvl[char]
  print(floor)


if __name__ == "__main__":
  main()
