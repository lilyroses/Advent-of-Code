# Solution 1 - Advent of Code 2025, Day 2



def main():
  INPUT_FILE = "input.txt"
  with open(INPUT_FILE, "r") as f:
    line = f.read().strip()

  id_ranges = []
  items = line.split(",")
  for item in items:
    id_ranges.append([int(id) for id in item.split("-")])

  for start, end in id_ranges:
    for num in range(start, end+1):
      i = 0  # num digits
      n = num
      while True:
        n = n // 10
        i += 1
        if n == 0:
          break
      if i % 2 == 0:
        print(i)


if __name__ == "__main__":
  main()
