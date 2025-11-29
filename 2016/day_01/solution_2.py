# Solution 2 - Advent of Code 2016, Day 1
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  instrs = lines[0].split(", ")

  cur = "N"
  x, y = 0, 0
  coords = []

  for i in instrs:
    dir = i[0]
    n = int(i[1:])

    if (cur == "N" and dir == "R") or (cur == "S" and dir == "L"):
      cur = "E"
      x += (1*n)

    elif (cur == "N" and dir == "L") or (cur == "S" and dir == "R"):
      cur = "W"
      x += (-1*n)

    elif (cur == "E" and dir == "R") or (cur == "W" and dir == "L"):
      cur = "S"
      y += (-1*n)

    else:
      cur = "N"
      y += (1*n)


  ans = abs(x) + abs(y)
  print(ans)


if __name__ == "__main__":
  main()
