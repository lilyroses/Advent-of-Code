# Solution 2 - Advent of Code 2015, Day 2

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  total_ribbon = 0
  for line in lines:
    L, W, H = sorted([int(n) for n in line.split('x')])
    total_ribbon += (L+L+W+W) + (L*W*H)
  print(total_ribbon)


if __name__ == "__main__":
  main()
