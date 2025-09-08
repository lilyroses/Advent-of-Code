# Solution 1 - Advent of Code 2015, Day 24

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  nums = [int(n) for n in lines]
  a = []
  b = []
  c = []

  x = 0
  n = sum(nums)
  m = n / 3

  for num in nums:
    if x + num <= m:
      x += num
      a.append(num)
      if x == m:
        break
    else:
      b.append(num)
  print(sum(a),b)


  a = list(range(1,6))
  b = list(range(7,12))
  print(sum(a)+sum(b))


if __name__ == "__main__":
  main()
