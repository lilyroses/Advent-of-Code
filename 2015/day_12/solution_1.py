# Solution 1 - Advent of Code 2015, Day 12
import json


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  total = 0
  d = json.loads(lines[0])
  s = lines[0]
  s = s.split(":")
  s = " ".join(s)
  s = s.split(",")
  s = " ".join(s)
  s = s.split("}")
  s = " ".join(s)
  s = s.split("{")
  s = " ".join(s)
  s = s.split("[")
  s = " ".join(s)
  s = s.split("]")
  s = " ".join(s)
  s = s.split()
  for i in s:
    if '"' not in i:
      total += int(i)

  print(total)

if __name__ == "__main__":
  main()
