# Solution 1 - Advent of Code 2017, Day 6
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  banks = [int(b) for b in lines[0].split("\t")]

  configs = []
  steps = 0

  def realloc(bank):
    i = banks.index(max(banks))
    alloc = banks[i]
    banks[i] = 0
    for j in range(alloc):
      i += 1
      i = i % len(banks)
      banks[i] += 1
    return banks

  while True:
    banks = realloc(banks)
    config = "-".join([str(b) for b in banks])
    steps += 1
    print(f"({steps})", config)

    if config not in configs:
      configs.append(config)
    else:
      print(f"FOUND INFINITE LOOP AFTER {steps} STEPS")
      return


if __name__ == "__main__":
  main()
