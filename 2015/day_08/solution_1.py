# Solution 1 - Advent of Code 2015, Day 8
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  eval_chars = 0
  print_chars = 0
  total_chars = 0
  for line in lines:
    print_chars += len(line)
    eval_chars += len(eval(line))
  print(print_chars - eval_chars)


if __name__ == "__main__":
  main()
