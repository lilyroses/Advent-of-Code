# Solution 1 - Advent of Code 2016, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  n = 0
  for line in lines:
    a,b,c, = [int(n) for n in line.split()]
    if (a+b > c) and (a+c > b) and (b+c > a):
      n += 1
  print(n)


if __name__ == "__main__":
  main()
