# Solution 1 - Advent of Code 2015, Day 20
from functools import reduce


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  max_presents = int(lines[0])
  presents_per_elf = 10


  def factor(n):
    return set(reduce(list.__add__, ([i, n//i] for i in
                      range(1, int(n**0.5)+1) if n % i == 0)))


  house_num = 0

  while True:
    house_num += 1
    visiting_elves = factor(house_num)

#    presents = sum(visiting_elves) * presents_per_elf
    presents = sum(visiting_elves)

    if house_num % 12345 == 0:
      print(f"{house_num:,}, {presents:,}")
#    print(f"{house_num:,}, {presents:,}")

    if presents >= max_presents // 10:  # div by 10 as each elf provides 10 presents - negates necessity of multiplying elf nums by 10 and thus finds solution somewhat faster (?)
      print(f"{house_num:,}, {presents:,}")
      break


if __name__ == "__main__":
  main()
