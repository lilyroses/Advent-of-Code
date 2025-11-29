# Solution 2 - Advent of Code 2018, Day 3
from collections import defaultdict as dd
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  coords = dd(int)
  ids = {}

  for line in lines:
    items = line.split()
    id = items[0]
    x, y = [int(n) for n in items[2][:-1].split(",")]
    w, h = [int(n) for n in items[-1].split("x")]

    for xx in range(x, x+w):
      for yy in range(-y, -y+-h,-1):  # y is -y because puzzle states y val is the inches from "top edge" of fabric
        coord = (xx, yy)
        coords[coord] += 1

  for line in lines:
    items = line.split()
    id = items[0]
    x, y = [int(n) for n in items[2][:-1].split(",")]
    w, h = [int(n) for n in items[-1].split("x")]

    overlaps = False
    for xx in range(x, x+w):
      for yy in range(-y, -y+-h,-1):  # y is -y because puzzle states y val is the inches from "top edge" of fabric
        coord = (xx,yy)
        if coords[coord] > 1:
          overlaps = True

    if not overlaps:
      print(id)


if __name__ == "__main__":
  main()

