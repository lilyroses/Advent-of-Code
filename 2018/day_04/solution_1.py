# Solution 1 - Advent of Code 2018, Day 4


def main():
  INPUT_FILE = "input.txt"
  with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]
  lines = sorted(lines)

  all_guard_data = []
  guard_data = []
  for line in lines:
    if "Guard" in line:
      if guard_data:
        all_guard_data.append(guard_data)
      guard_data = [line]
    else:
      guard_data.append(line)
  all_guard_data.append(guard_data)

  sleep_data = {}
  for guard_data in all_guard_data:
    id = int(guard_data[0].split()[3][1:])
    sleep_times = []
    for line in guard_data[1:]:
      min = int(line.split()[1][:-1].split(":")[1])
      if "asleep" in line:
        start = min
      elif "wakes" in line:
        stop = min
        sleep_times.append((start, stop))
    if sleep_times:
      if id not in sleep_data:
        sleep_data[id] = dd(int)
      for start, stop in sleep_times:
        for min in range(start, stop):
          sleep_data[id][min] += 1


  id_totals = {}
  for id, min_counts in sleep_data.items():
    if id not in id_totals:
      id_totals[id] = dd(int)
    t = sum(min_counts.values())

    id_totals[id]
    id_sleep_totals[id] += t

    for min, ind in enumerate(mins_asleep):
      if ind == "#":
        id_sleep_mins[id][min] += 1

  max_time_asleep = 0
  id_sleep_most = ""
  for id, t in id_sleep_totals.items():
    if t > max_time_asleep:
      max_time_asleep = t
      id_sleep_most = id

  freq_count = max(id_sleep_mins[id_sleep_most].values())
  for min, count in id_sleep_mins[id_sleep_most].items():
    if count == freq_count:
      freq_min = min
  id = int(id_sleep_most[1:])
  print(id*freq_min)


if __name__ == "__main__":
  main()

