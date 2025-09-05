# Solution 2 - Advent of Code 2016, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0,'A','B','C',0],
    [0, 0, 'D', 0, 0]
  ]

  max_row = 4
  max_col = 4
  row = 2
  col = 0

  nums = ""

  for line in lines:
    for char in line:

      if char == "R":
        pcol = min(max_col, col+1)
        if keypad[row][pcol] != 0:
           col = pcol

      elif char == "L":
        pcol = max(0, col-1)
        if keypad[row][pcol] != 0:
          col = pcol

      elif char == "D":
        prow = min(max_row, row+1)
        if keypad[prow][col] != 0:
          row = prow

      elif char == "U":
        prow = max(0, row-1)
        if keypad[prow][col] != 0:
          row = prow

    nums += str(keypad[row][col])

  print(nums)


if __name__ == "__main__":
  main()
