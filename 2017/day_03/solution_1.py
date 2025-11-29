# Solution 1 - Advent of Code 2017, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
  target = int(lines[0])

  ring = 1
  min_val = 1
  max_val = 1
  num_to_square = 1
  edge_len = 1

  while True:
    ring += 1
    num_to_square += 2
    min_val = max_val + 1
    max_val = num_to_square**2

    edge_len += 2
    rv = list(range(min_val, min_val+(edge_len-1))
    rv.insert(0,max_val)
    rv = sorted(rv, reverse=True)

    th = list(range(rv[0], rv[0]+edge_len))
    th = sorted(th, reverse=True)

    lv = list(range(th[0], th[0]+edge_len))

    bh = list(range(lv[-1], max_val+1))

    print(th)
    fo
      print(f"{rv[i+1

    if target in range(min_val, max_val+1):
      print(ring)
      break



if __name__ == "__main__":
  main()
