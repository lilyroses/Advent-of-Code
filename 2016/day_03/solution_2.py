# Solution 2 - Advent of Code 2016, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  arr = [[int(n) for n in line.lstrip().split()] for line in lines]

  total = 0
  for i in range(0, len(arr), len(arr[0])):
    a,b,c = arr[i:i+len(arr[0])]
    for j in range(len(arr[0])):
      if (
           ((a[j] + b[j]) > c[j])
           and ((a[j] + c[j]) > b[j])
           and ((b[j]+c[j]) > a[j])
      ):
        total += 1

  print(total)


if __name__ == "__main__":
  main()
