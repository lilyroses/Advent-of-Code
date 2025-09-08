# Solution 1 - Advent of Code 2015, Day 25
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  inpt = lines[0].split()
  max_row = int(inpt[-3][:-1])
  max_col = int(inpt[-1][:-1])

<<<<<<< HEAD
  GRID_FILE = "grid.txt"
  with open(GRID_FILE, "r") as f:
    grid_lines = [line.strip() for line in f.readlines()]
  base_grid = [[int(n) for n in line.split()]
                for line in grid_lines]

#  for row in base_grid:
#    print(row)

#  print(base_grid[5][5])

  def get_next_num(pnum):
    pass

  def update_grid(grid, prow, pcol):
    pnum = grid[prow][pcol]
#    nnum = (pnum * 5) - 1
    nnum = pnum + 5

    # if prev row was 0, add a new row
    if prow == 0:
      nrow = pcol + 1
      ncol = 0
      grid.append([nnum])
    else:
      nrow = prow - 1
      ncol = pcol + 1
      grid[nrow].append(nnum)
    return grid, nrow, ncol

  max_row = 3010
  max_col = 3019
=======
>>>>>>> f00759a2d75d3b81fdfa1f74a5ec08fb52ad4d2b
  x = 20151125
  y = 252533
  z = 33554393

  row = 1
  col = 1

<<<<<<< HEAD
  row, col = 0, 0
  while True:
    grid, row, col = update_grid(grid, row, col)
    if len(grid) == 6:
#      if len(grid[max_row]) >= max_col:
#        answer = grid[max_row-1][max_col-1]
#        answer = len(grid[max_row-1])
        break

#  print(answer)
  for row in grid:
    print(row)
=======
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
>>>>>>> f00759a2d75d3b81fdfa1f74a5ec08fb52ad4d2b


if __name__ == "__main__":
  main()
