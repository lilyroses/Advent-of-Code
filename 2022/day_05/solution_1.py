# Solution 1 - Advent of Code 2022, Day 5

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = f.readlines()


def main():
  stacks = [[] for i in range(9)]
  instrs = []

  for line in lines:
    if "move" in line:
      instrs.append(line)
    elif "[" in line:
      crates = ["." if line[i] == " " else line[i] for i in range(1,len(line),4)]
      for i, crate in enumerate(crates):
        if crate != ".":
          stacks[i].insert(0,crate)


  for instr in instrs:
    print(instr)
    items = instr.split()
    num_crates = int(items[1])
    # indices of start stack, end stack within stacks list
    i = int(items[3]) - 1
    j = int(items[5]) - 1
    for i in range(num_crates):
      crate = stacks[i].pop()
      stacks[j].append(crate)

  s = ""
  for stack in stacks:
⁴⁴    c = stack[-1]
    s += c
  print(s)


if __name__ == "__main__":
  main()

