# Solution 2 - Advent of Code 2015, Day 9
from collections import defaultdict as dd
from itertools import permutations as perms

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  longest_distance = 0
  cities = []
  city_distances = dd(dict)

  for line in lines:
    city1, city2, distance = line.split()[::2]
    distance = int(distance)

    cities.append(city1)
    cities.append(city2)

    city_distances[city1][city2] = distance
    city_distances[city2][city1] = distance

  cities = set(cities)
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
    if longest_distance == 0:
      longest_distance = total_distance
    else:
      longest_distance = max(longest_distance, total_distance)

  print(longest_distance)


if __name__ == "__main__":
  main()
