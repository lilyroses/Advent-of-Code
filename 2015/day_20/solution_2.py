# Solution 2 - Advent of Code 2015, Day 20
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  max_presents = int(lines[0])
  presents_per_elf = 11
  house_presents = dd(int)

  elf_num = 0
  while True:
    elf_num += 1

    house_nums = [elf_num*i for i in range(1,51)]
    print(f"\nElf {elf_num}: {house_nums}")

    for house in house_nums:
      presents = elf_num * presents_per_elf
      house_presents[house] += presents

      print(f"\t{house}: {house_presents[house]}")

      if house_presents[house] >= max_presents:
        print(house)
        break


if __name__ == "__main__":
  main()
