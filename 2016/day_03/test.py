OUTPUT_FILE = "input2.txt"

with open("input.txt", "r") as f:
  txt = f.read().split("\n")

arr = [[int(n) for n in line.lstrip().split()] for line in txt]


