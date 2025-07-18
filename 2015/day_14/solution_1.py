# Solution 1 - Advent of Code 2015, Day 14

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  
  seconds = 2503
  reindeer_distances = {}

  for line in lines:
    distance = 0
    time = 0

    items = line.split()
    reindeer_name = items[0]
    flight_km = int(items[3])
    flight_s = int(items[6])
    rest_s = int(items[13])

    while time < seconds:
      #  b
      for i in range(flight_s):
        time += 1
        if time == seconds:
          break
        else:
          distance += flight_km
      for i in range(rest_s):
        time += 1
        if time == seconds:
          break

    reindeer_distances[reindeer_name] = distance

  winning_distance = max(reindeer_distances.values())
  print(winning_distance)
  for r, d in reindeer_distances.items():
    print(r, d)


if __name__ == "__main__":
  main()
