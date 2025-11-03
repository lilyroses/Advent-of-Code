# Solution 1 - Advent of Code 2016, Day 1
INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  instrs = lines[0].split(", ")
  print(instrs)

  cur = "N"
  x, y = 0, 0
  print(f"Start: CUR={cur} COORDS={(x,y)}")

  for i in instrs:
    dir = i[0]
    n = int(i[1:])

    if cur == "N":
      if dir == "R":
        cur = "E"
        x += n
      elif dir == "L":
        cur = "W"
        x -= n
    elif cur == "E":
      if dir == "R":
        cur = "S"
        y -= n
      elif dir == "L":
        cur = "N"
        y += n
    elif cur == "S":
      if dir == "R":
        cur = "W"
        x -= n
      elif dir == "L":
        cur = "E"
        x += n
    elif cur == "W":
      if dir == "R":
        cur = "N"
        y += n
      elif dir == "L":
        cur = "S"
        y -= n


  ans = abs(x) + abs(y)
  print(ans)


if __name__ == "__main__":
  main()
