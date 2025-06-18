# Solution 1 - Advent of Code 2015, Day 6
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  GRID = [[0 for i in range(1000)]
             for j in range(1000)]
  total = 0

  for i, line in enumerate(lines, 1):
    print(f"EXECUTING LINE {i}/{len(lines)}...")
    items = line.split()
    instr = items[:-3][-1]
    coord_1 = [int(i) for i in items[-3].split(",")]
    coord_2 = [int(i) for i in items[-1].split(",")]

    start_row, end_row = coord_1[1], coord_2[1]
    start_idx, end_idx = coord_1[0], coord_2[0]

    for row in range(start_row, end_row+1):
      for i in range(start_idx, end_idx+1):
        if GRID[row][i] == 1 and instr != "on":
          GRID[row][i] = 0
          total -= 1
        elif GRID[row][i] == 0 and instr != "off":
          GRID[row][i] = 1
          total += 1
  print(total)


if __name__ == "__main__":
  main()

