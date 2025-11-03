# Solution 2 - Advent of Code 2016, Day 5
from hashlib import md5
from string import digits


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  door_id = lines[0]
  pwd = ["_" for i in range(8)]

  i = 0
  while True:
    s = door_id+str(i)
    hash = md5(s.encode()).hexdigest()

    if hash.startswith("00000"):
      pos = hash[5]
      if pos in digits:
        pos = int(pos)
        if pos in range(len(pwd)) and pwd[pos] == "_":
          pwd[pos] = hash[6]

          print(f"\nFOUND HASH AT POS {pos}\n")

          if "_" not in pwd:
            break

    i += 1

  print("".join(pwd))


if __name__ == "__main__":
  main()
