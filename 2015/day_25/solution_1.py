# Solution 1 - Advent of Code 2015, Day 25
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  inpt = lines[0].split()
  max_row = int(inpt[-3][:-1])
  max_col = int(inpt[-1][:-1])

  x = 20151125
  y = 252533
  z = 33554393

  row = 1
  col = 1

  while True:

    if row == 1:
      row = col + 1
      col = 1
    else:
      row -= 1
      col += 1
    x = (x*y) % z

    if row % 1000 == 0:
      print(f"row={row}, col={col}")

    if row == max_row and col == max_col:
      print("\nFOUND:", x)
      break


if __name__ == "__main__":
  main()
