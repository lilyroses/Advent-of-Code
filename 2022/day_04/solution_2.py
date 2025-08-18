# Solution 2 - Advent of Code 2022, Day 4
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  total = 0

  for line in lines:
    p1, p2 = line.split(",")
    a, b = [int(n) for n in p1.split("-")]
    c, d = [int(n) for n in p2.split("-")]

    if (
         (a >= c and a <= d) or
         (b >= c and b <= d) or
         (c >= a and c <= b) or
         (d >= a and d <= b)
    ):
      total += 1

  print(total)


if __name__ == "__main__":
  main()
