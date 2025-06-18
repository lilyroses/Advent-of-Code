# Solution 2 - Advent of Code 2015, Day 3
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  chars = list(lines[0])
  dirs = {"^": [0, 1], ">": [1,0], "v": [0, -1], "<": [-1, 0]}
  x, y = 0, 0
  rx, ry = 0, 0
  houses = [f"{x} {y}"]

  for i, char in enumerate(chars):
    dx, dy = dirs[char]
    if i % 2 == 0:
      x += dx
      y += dy
      house = f"{x} {y}"
    else:
      rx += dx
      ry += dy
      house = f"{rx} {ry}"
    if house not in houses:
      houses.append(house)
  print(len(houses))


if __name__ == "__main__":
  main()
