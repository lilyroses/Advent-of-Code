# Solution 2 - Advent of Code 2025, Day 1

def main():
  INPUT_FILE = "input.txt"
  with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]

  dial = 50
  total = 0
  for line in lines:
    dir = line[0]
    notches = int(line[1:])
    n = 1
    if dir == "L":
      n = -n
    for i in range(+notches):
      dial += n
      if dial == 0:
        total += 1
      elif dial == -1:
        dial = 99
      elif dial == 100:
        dial = 0
        total += 1
  print(total)


if __name__ == "__main__":
  main()
