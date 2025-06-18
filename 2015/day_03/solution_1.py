# Solution 1 - Advent of Code 2015, Day 3
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  chars = list(lines[0])
  dirs = {"^": [0, 1], ">": [1,0], "v": [0, -1], "<": [-1, 0]}
  x, y = 0,0
  houses = [f"{x} {y}"]

  for char in chars:
    x += dirs[char][0]
    y += dirs[char][1]
    house = f"{x} {y}"
    if house not in houses:
      houses.append(house)
  print(len(houses))


if __name__ == "__main__":
  main()
