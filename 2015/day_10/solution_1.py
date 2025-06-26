# Solution 1 - Advent of Code 2015, Day 10
from itertools import groupby

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  s = lines[0]

  seqs = {}

  for i in range(1,4):
    for j in range(1,4):
      # 1, 11, 111, 2, 22, 222, 3, 33, 333
      chars = str(i)*j
      seqs[chars] = str(len(chars)) + chars[0]

  def look_say(seq):
    digits = [''.join(c) for _, c in groupby(seq)]
    s = ""
    for seq in digits:
      s += seqs[seq]
    return s

  for i in range(40):
    s = look_say(s)
  print(len(s))


if __name__ == "__main__":
  main()
