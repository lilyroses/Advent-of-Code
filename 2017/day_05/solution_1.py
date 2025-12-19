# Solution 1 - Advent of Code 2017, Day 5

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  instrs = [int(i) for i in lines]
  steps = 0

  cur_idx = 0

  while True:
    val = instrs[cur_idx]
    new_idx = cur_idx + val
    val += 1
    instrs[cur_idx] = val
    cur_idx = new_idx
    steps += 1
    if cur_idx >= len(instrs):
      break

  print(steps)


if __name__ == "__main__":
  main()
