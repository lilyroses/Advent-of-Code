# Solution 1 - Advent of Code 2015, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  total_paper = 0
  for line in lines:
    L, W, H = sorted([int(n) for n in line.split('x')])
    total_paper += ((2*L*W) + (2*W*H) + (2*L*H)) + (L*W)
  print(total_paper)


if __name__ == "__main__":
  main()
