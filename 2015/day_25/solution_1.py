# Solution 1 - Advent of Code 2015, Day 25
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  inpt = lines[0].split()
  row = int(inpt[-3][:-1])
  col = int(inpt[-1][:-1])

  def get_next_num(pnum):
    
  def update_grid(grid, prow, pcol):
    pnum = grid[prow][pcol]
    nnum = pnum + 1

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

  grid = [[1]]
  row, col = 0, 0
  while len(grid) < 10:
    grid, row, col = update_grid(grid, row, col)

  for row in grid:
    print(row)


if __name__ == "__main__":
  main()
