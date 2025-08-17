# Solution 1 - Advent of Code 2022, Day 4
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  total = 0

  for line in lines:
    p1, p2 = line.split(",")
    a, b = [int(n) for n in p1.split("-")]
    c, d = [int(n) for n in p2.split("-")]

    p1_in_p2 = (
      (a >= c and a <= d) and
      (b >= c and b <= d)
    )

    p2_in_p1 = (
      (c >= a and c <= b) and
      (d >= a and d <= b)
    )

    if p1_in_p2 or p2_in_p1:
      total += 1

  print(total)


if __name__ == "__main__":
  main()
