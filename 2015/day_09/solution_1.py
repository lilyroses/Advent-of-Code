# Solution 1 - Advent of Code 2015, Day 9
from collections import defaultdict as dd
from itertools import permutations as perms


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  shortest_distance = 0
  cities = []
  city_distances = dd(dict)
  for line in lines:
    items = line.split()
    city1 = items[0]
    city2 = items[2]
    distance = int(items[-1])

    if city1 not in cities:
      cities.append(city1)
    if city2 not in cities:
      cities.append(city2)

    city_distances[city1][city2] = distance
    city_distances[city2][city1] = distance

  travel_perms = perms(cities)
  for t in travel_perms:
    total_distance = 0
    journey = " ".join(t).split()
    start_cities = journey[:-1]
    end_cities = journey[1:]
    for i in range(len(start_cities)):
      start = start_cities[i]
      end = end_cities[i]
      total_distance += city_distances[start][end]
    if shortest_distance == 0:
      shortest_distance = total_distance
    else:
      shortest_distance = min(shortest_distance, total_distance)
  print(shortest_distance)

if __name__ == "__main__":
  main()
