# Solution 1 - Advent of Code 2016, Day 4
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  total = 0

  for line in lines:
    items = line.split("-")
    room_letters = items[:-1]
    sector_id, checksum = items[-1].split("[")
    sector_id = int(sector_id)
    checksum = checksum[:-1]

    counts = dd(int)
    for letters in room_letters:
      for letter in letters:
        counts[letter] += 1
    vals = sorted(set(counts.values()),reverse=True)
    s = ""

    # for each value in the list of highest values
    for val in vals:
      # make a list of chars with that value
      chars = []
      for k, v in counts.items():
        if v == val:
          chars.append(k)

      # sort the list of characters
      chars = sorted(chars)
#      print(chars)
      # one at a time, add chars to s
      for char in chars:
        if len(s) < 5:
          s += char
      if len(s) == 5:
        break

    if sorted(checksum) == sorted(s):
      total += sector_id

  print(total)


if __name__ == "__main__":
  main()
