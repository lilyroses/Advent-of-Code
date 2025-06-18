# Solution 1 - Advent of Code 2015, Day 5

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  def has_three_vowels(s):
    VOWELS = list("aeiou")
    vowel_count = sum([1 for c in s if c in VOWELS])
    return vowel_count >= 3

  def has_double_char(s):
    pairs = []
    for i in range(len(s)-1):
      if s[i] == s[i+1]:
        return True
    return False

  def devoid_illegal_substrs(s):
    ILLEGAL_SUBSTRS = "ab cd pq xy".split()
    for substr in ILLEGAL_SUBSTRS:
      if substr in s:
        return False
    return True

  total = 0
  for s in lines:
    if (
      has_three_vowels(s)
      and has_double_char(s)
      and devoid_illegal_substrs(s)
    ):
      total += 1
  print(total)


if __name__ == "__main__":
  main()
