grid = [[1]]
r, c = 0,0
n = grid[r][c]

while True:
  n += 1
  if r == 0:
    r += 1
    c = 0
    grid.append([n])
  else:
    r -= 1
    c += 1
    grid[r].append(n)
  if len(grid) == 10:
    break

for row in grid:
  print(row)
