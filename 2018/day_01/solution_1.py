# Solution 1 - Advent of Code 2018, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  f = 0
  for line in lines:
    i = int(line)
    f += i
  print(f)


if __name__ == "__main__":
  main()
