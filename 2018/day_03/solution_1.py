# Solution 1 - Advent of Code 2018, Day 3
from collections import defaultdict as dd
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  coords = dd(int)

  for line in lines:
    items = line.split()
    id = items[0]
    x, y = [int(n) for n in items[2][:-1].split(",")]
    w, h = [int(n) for n in items[-1].split("x")]

    for xx in range(x, x+w):
      for yy in range(-y, -y+-h,-1):  # y is -y because puzzle states y val is the inches from "top edge" of fabric
        coord = (xx, yy)
        coords[coord] += 1

  t = 0
  for coord, count in coords.items():
    if count > 1:
      t += 1

  print(t)


if __name__ == "__main__":
  main()

