# Solution 2 - Advent of Code 2018, Day 4

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

  rows = []
  ids = []
  for guard_data in all_guard_data:
    id = guard_data[0].split()[3]
    ids.append(id)

    sleep_times = []
    for line in guard_data[1:]:
      items = line.split()
      date = items[0][6:]
      hr, min = [int(n) for n in items[1][:-1].split(":")]
      sleep_data = ["." for i in range(60)]
      if "asleep" in line:
        sleep_start = min
      elif "wakes" in line:
        sleep_stop = min
        sleep_times.append((sleep_start, sleep_stop))

    if sleep_times:
      for start_sleep, stop_sleep in sleep_times:
        for min in range(start_sleep, stop_sleep):
          sleep_data[min] = "#"

    sleep_data = "".join(sleep_data)
    row = [date, id, sleep_data]
    rows.append(row)

  ids = set(ids)
  id_sleep_totals = {}
  for id in ids:
    id_sleep_totals[id] = 0

  id_sleep_mins = {}
  for id in ids:
    id_sleep_mins[id] = {}
    for i in range(60):
      id_sleep_mins[id][i] = 0

  for row in rows[3:]:

    date, id, mins_asleep = row
    t = mins_asleep.count("#")
    id_sleep_totals[id] += t

    for min, ind in enumerate(mins_asleep):
      if ind == "#":
        id_sleep_mins[id][min] += 1


  id_min_asleep_most = {}
  for id in ids:
    id_min_asleep_most[id] = {}
    for i in range(60):
      id_min_asleep_most[id][i] = 0

  for id, mins in id_sleep_mins.items():
    id_min_asleep_most[id] = {}
    cur_max_min = 0
    cur_count = 0
    for min, count in mins.items():
      if count > cur_count:
        cur_max_min = min
        cur_count = count
        id_min_asleep_most[id][cur_max_min] = cur_count

  maxes = {}
  for id, mins in id_min_asleep_most.items():
    max_count = max(mins.values())
    for min, count in mins.items():
      if count == max_count:
        maxes[id] = [min, count]

  id_max = ""
  min_max = 0
  cur = 0
  for id, m in maxes.items():
    min = m[0]
    count = m[1]
    if count > cur:
      cur = count
      min_max = min
      id_max = id

  print(id_max, min_max, cur)


if __name__ == "__main__":
  main()

