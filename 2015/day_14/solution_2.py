# Solution 2 - Advent of Code 2015, Day 14
from collections import defaultdict as dd 


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  seconds = 2503
  reindeer_distances = dd(list)
  reindeer_points = dd(int)

  for line in lines:
    distance = 0
    time = 0 
    items = line.split()
    reindeer_name = items[0]
    flight_km = int(items[3])
    flight_s = int(items[6])
    rest_s = int(items[13])

    while time < seconds:

      for i in range(flight_s):
        time += 1
        if time == seconds:
          break
        else:
          distance += flight_km
          reindeer_distances[reindeer_name].append(distance)

      for i in range(rest_s):
        time += 1
        if time == seconds:
          break
        else:
          reindeer_distances[reindeer_name].append(distance)

  for i in range(seconds-1):
    current_distances = []

    for reindeer, distances in reindeer_distances.items():
      current_distances.append(distances[i])
      
    w = max(current_distances)
    for reindeer, distances in reindeer_distances.items():
      if distances[i] == w:
        reindeer_points[reindeer] += 1

  print(max(reindeer_points.values()))


if __name__ == "__main__":
  main()
