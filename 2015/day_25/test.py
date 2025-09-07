max_rows = 3010
max_cols = 3019

grid = [[1 for i in range(max_cols)]
           for j in range(max_rows)]

print(grid[max_rows-1][max_cols-1])

grid = [
  [1, 3, 6, 10, 15, 21],
  [2, 5,  9, 14, 20],
  [4, 8, 13, 19],
  [7, 12, 18],
  [11, 17],
  [16]
]

#grid = [[1]]
row = 0
col = 0
pnum = 1

def u(row, col, grid):
  pnum = grid[row][col]
  nnum = pnum + 1
  if row == 0:
    row += 1
    col = 0
    grid.append([nnum])

  else:
    row -= 1
    col += 1
    grid[row].append(nnum)

  return row, col, grid


n = len(grid)
for i in range(n):
  print(grid[i])
