# Solution 2 - Advent of Code 2015, Day 7
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  wire_ids = {"b": 16076}

  # remove lines as executed to iteratively handle all instructions
  while lines:
    for line in lines:
      items = line.split()
      output_wire = items[-1]
      input_items = []
      # input items might be wire_id key or digit string
      input_values = []
      op = ''

      if "NOT" in items:
        input_items.append(items[1])
        op = items[0]

      elif len(items) == 3 and "-> b" in line:
        lines.remove(line)
        continue

      else:
        # instructions with 3 items, e.g. 'x -> 123' are just assignment instructions (no op)
        input_items.append(items[0])

        if len(items) > 3:
          # instructions longer than 3 items have operations
          input_items.append(items[2])
          op = items[1]

      # ensure the order of the inputs stays the same
      input_values = ['' for i in input_items]
      for i, item in enumerate(input_items):
        if item.isdigit():
          input_value = int(item)
          input_values[i] = input_value
        elif item in wire_ids:
          input_value = wire_ids[item]
          input_values[i] = input_value

      # if every input item corresponds to a numeric value, the line is executable
      if '' not in input_values:
        if not op:
          input_val = input_values[0]
        elif op == "NOT":
          input_val = ~input_values[0] & 65535
        elif op == "AND":
          input_val = input_values[0] & input_values[1]
        elif op == "OR":
          input_val = input_values[0] | input_values[1]
        elif op == "LSHIFT":
          input_val = input_values[0] << input_values[1]
        elif op == "RSHIFT":
          input_val = input_values[0] >> input_values[1]

        wire_ids[output_wire] = input_val
        lines.remove(line)

  print(wire_ids["a"])


if __name__ == "__main__":
  main()
