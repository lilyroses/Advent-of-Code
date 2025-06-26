# Solution 2 - Advent of Code 2015, Day 8
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  original_chars = 0
  new_chars = 0
  for line in lines:
    new_line = line.replace("\\", "\\\\").replace(r'"', r'\"')
    original_chars += len(line)
    new_chars += (len(new_line)+2)
  print(new_chars - original_chars)

if __name__ == "__main__":
  main()
