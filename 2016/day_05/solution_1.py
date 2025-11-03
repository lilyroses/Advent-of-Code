# Solution 1 - Advent of Code 2016, Day 5
from hashlib import md5


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  i = 0
  door_id = lines[0]

  pwd = ""
  while True:
    s = door_id+str(i)
    hash = md5(s.encode()).hexdigest()

    if hash.startswith("00000"):
      pwd += hash[5]
      print(f"\nFOUND HASH #{len(pwd)}\n")

    if len(pwd) == 8:
      break

    i += 1

  print(pwd)


if __name__ == "__main__":
  main()
