# Solution 1 - Advent of Code 2016, Day 2

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  keypad = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]

  max_row = 2
  max_col = 2
  row = 1
  col = 1

  nums = ""

  for line in lines:
    for char in line:
      if char == "R":
        col = min(max_col, col+1)
      elif char == "L":
        col = max(0, col-1)
      elif char == "D":
        row = min(max_row, row+1)
      elif char == "U":
        row = max(0, row-1)
    nums += str(keypad[row][col])

  print(nums)


if __name__ == "__main__":
  main()
