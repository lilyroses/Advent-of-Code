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

  col = 1
  row = 1
  max_row = 2
  max_col = 2

  nums = ""

  for line in lines:
    instrs = list(line)
    for instr in instrs:
      if instr == "R":
        col = min(col+1, max_col)
      elif instr == "L":
        col = max(0, col-1)
      elif instr == "U":
        row = max(0, row-1)
      elif instr == "D":
        row = min(max_row, row+1)
#      print(keypad[row][col])

    num = keypad[row][col]
    nums += str(num)

  print(nums)

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
