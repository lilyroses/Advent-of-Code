# Solution 1 - Advent of Code 2016, Day 4
from collections import defaultdict as dd
<<<<<<< HEAD
=======
from itertools import groupby
>>>>>>> c6569d7ae690c569d4242eac22cc72692afad02a


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
<<<<<<< HEAD
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
=======

    total = 0

    for line in lines:
        room_id = line.split("-")
        name = "".join(room_id[:-1])
        sector_id = int(room_id[-1].split("[")[0])
        checksum = room_id[-1].split("[")[1][:-1]
        
        letter_groups = sorted([''.join(g) for _, g in groupby(sorted(name))], reverse=True, key=len)

        check = ""
        for s in letter_groups[:5]:
            c = s[0]
            check += c

        if check == checksum:
            total += sector_id

    print(total)
>>>>>>> c6569d7ae690c569d4242eac22cc72692afad02a


if __name__ == "__main__":
    main()
