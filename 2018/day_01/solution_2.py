# Solution 2 - Advent of Code 2018, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]

#lines = [+3, 3, 4, -2, -4]

def main():
  f = 0
  vals = [f]

  i = 0
  while True:
    num = int(lines[i])
    print(f"{f} + {num} = {f+num}")
    f += num
    if f not in vals:
      vals.append(f)
    elif f in vals:
      return f
    i += 1
    i = i % len(lines)


if __name__ == "__main__":
  main()
