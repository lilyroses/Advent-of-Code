# Solution 1 - Advent of Code 2018, Day 2
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  letters_2 = 0
  letters_3 = 0

  for word in lines:
    letter_counts = dd(int)
    for letter in word:
      letter_counts[letter] += 1

    if 2 in letter_counts.values():
      letters_2 += 1
    if 3 in letter_counts.values():
      letters_3 += 1

  print(letters_2*letters_3)


if __name__ == "__main__":
  main()
