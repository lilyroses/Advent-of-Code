# Solution 1 - Advent of Code 2015, Day 15
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


for d in range()
def allocs(n):
    # n = 10
    # allocs = [
    
    # d = n (10)
    # c = n - d
    # while (d > c):
    #   c += 1
    #   d -= 1

    # LOOP 0:
      # d = 10  (d = n : d =  10)
      # c = 0   (n - d : 10 - 10)

    # LOOP 1:
      # d = 9   (d - 1 : 10 - 1)
      # c = 1   (c + 1 :  0 + 1)

    # LOOP 2:
      # d = 8
      # c = 2

    # LOOP 3:
      # d = 7
      # c = 3

    # ...

    # LOOP 10
      # d = 0
      # c = 10 (c + 1 : 9 + 1)

    d = n
    c = n - d
    b = n - (d + c)
    a = n - (d + c + b)
    

    #   [0, 0, 0, 10],

    #   [0, 0, 1, 9],
    #   [0, 0, 2, 8],
    #   [0, 0, 3, 7],
    #   ...
    #   [0, 0, 10, 0]

    #   [0, 1, 0, 9]
    #   [0, 1, 1, 8]
    #   [0, 1, 2, 7]
    #   [0, 1, 3, 6]
    #   [0, 1, 4, 5]
    #   [0, 1, 5, 4]
    #   [0, 1, 6, 3]
    #   [0, 1, 7, 2]
    #   [0, 1, 8, 1]
    #   [0, 1, 9, 0]
    allocs = []

    for 


def main():
    ingrs = dd(list)

    for line in lines:
        items = line.split()
        ingr = items[0][:-1]
        values = [int(items[i][:-1]) if "," in items[i] else int(items[i])
                  for i in range(2, len(items), 2)]
        ingrs[ingr] = values

    for k, v in ingrs.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
