# Solution 2 - Advent of Code 2018, Day 4
from collections import defaultdict as dd


def main():
  INPUT_FILE = "input.txt"
  with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]
  lines = sorted(lines)

  all_guard_lines = []
  guard_lines = []
  for line in lines:
    if "Guard" in line:
      if guard_lines:
        all_guard_lines.append(guard_lines)
      guard_lines = [line]
    else:
      guard_lines.append(line)
  all_guard_lines.append(guard_lines)

  sleep_data = {}
  for guard_lines in all_guard_lines:
    id = int(guard_lines[0].split()[3][1:])
    for line in guard_lines[1:]:
      items = line.split()
      min = int(line.split()[1][:-1].split(":")[1])
      if "asleep" in line:
        start = min
      elif "wakes" in line:
        stop = min
        if id not in sleep_data:
          sleep_data[id] = dd(int)
        for min in range(start, stop):
          sleep_data[id][min] += 1

  id, min_count = max(sleep_data.items(), key=lambda item: max(item[1].values()))
  min, count = max(min_count.items(), key=lambda item: item[1])
  print(id * min)


if __name__ == "__main__":
  main()

