# Solution 1 - Advent of Code 2015, Day 15

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  total_tsps = 100
  allocs = []
  a = 0
  b = 0
  c = 0
  d = 100
  alloc = [a,b,c,d]
  allocs.append(alloc)
  while d > 0:
    c += 1
    d -= 1
    allocs.append([a,b,c,d])
  while b < total_tsps:
    b += 1
    c -

if __name__ == "__main__":
  main()
