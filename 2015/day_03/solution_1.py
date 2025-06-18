# Solution 1 - Advent of Code 2015, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  chars = list(lines[0])
  dirs = {
    "^": [0, 1],
    ">": [1,0],
    "v": [0, -1],
    "<": [-1, 0]
  }

  x, y = 0,0
  start_house = f"{x}{y}"
  houses = [start_house]

  for char in chars:
    x += dirs[char][0]
    y += dirs[char][1]
    new_house = f"{x}{y}"
    if new_house not in houses:
      houses.append(new_house)
  print(len(houses))





if __name__ == "__main__":
  main()
