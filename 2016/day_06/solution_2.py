# Solution 2 - Advent of Code 2016, Day 6
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  cols = len(lines[0])
  msgs = []
  for c in range(cols):
    s = ""
    for line in lines:
      s  += line[c]
    msgs.append(s)

  s = ""
  for msg in msgs:
    c = {}
    for letter in msg:
      if letter not in c:
        c[letter] = 1
      else:
        c[letter] += 1
    max_c = min(c.values())
    for char, v in c.items():
      if v == max_c:
        s += char

  print(s)


if __name__ == "__main__":
  main()
