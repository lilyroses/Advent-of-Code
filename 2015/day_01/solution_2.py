# Solution 1 - Advent of Code 2015, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  chars = list(lines[0])
  lvl = {"(": 1, ")":-1}
  floor = 0
  for i, char in enumerate(chars, 1):
    floor += lvl[char]
    if floor == -1:
      print(i)
      break


if __name__ == "__main__":
  main()
