# Solution 2 - Advent of Code 2016, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  arr = [[int(n) for n in line.lstrip().split()] for line in lines]

  num_rows = len(arr)
  num_cols = len(arr[0])
  for row in arr[1:]:
    if len(row) != num_cols:
      print("Error")
      return False

  new_arr = [[] for i in range(num_cols)]
  for i in range(num_rows):
    for j in range(num_cols):
      num = arr[i][j]
      new_arr[j].append(num)

  total = 0

  for row in new_arr:
    for i in range(0, len(row),3):
      a, b, c = row[i:i+3]
      if (a+b > c) and (a+c > b) and (b+c > a):
        total += 1

  print(total)


if __name__ == "__main__":
  main()
