# Solution 1 - Advent of Code 2022, Day 11

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  ms = {}

  idxs = []
  for i, line in enumerate(lines):
    if "M" in line:
      idxs.append(i)

      num = int(line.split()[-1][:-1])
      ms[num] = {}
      ms[num]["items"] = []

  


if __name__ == "__main__":
  main()
