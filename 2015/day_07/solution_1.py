# Solution 1 - Advent of Code 2015, Day 7
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  wire_vals = {}
  #while lines:
  for line in lines:
    items = line.split()
    if len(items) == 3:
      input_val = int(items[0])
      output_wire = items[-1]
      wire_vals[output_wire] = input_val
      lines.remove(line)
    elif len(items) == 4:
      ,
    print(items[-4])



if __name__ == "__main__":
  main()
