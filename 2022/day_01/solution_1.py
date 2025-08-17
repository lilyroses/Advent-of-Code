# Solution 1 - Advent of Code 2022, Day 1
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  groups = []
  group = []

  for line in lines:
    if line:
      group.append(int(line))
    else:
      groups.append(sum(group))
      group = []
  groups.append(sum(group))

  groups = sorted(groups, reverse=True)
  answer = groups[0]
  print(answer)


if __name__ == "__main__":
  main()
