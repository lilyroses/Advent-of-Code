# Solution 2 - Advent of Code 2015, Day 4
from hashlib import md5

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  substr = "000000"
  i = 0
  while True:
    txt = f"{lines[0]}{i}"
    hash = md5(txt.encode()).hexdigest()
    if hash.startswith(substr):
      print(i)
      return
    i += 1

if __name__ == "__main__":
  main()
