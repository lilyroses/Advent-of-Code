# Solution 2 - Advent of Code 2015, Day 5
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  def has_double_pair(s):
    pairs = {}
    for i in range(len(s)-1):
      pair = s[i:i+2]
      if pair not in pairs:
        pairs[pair] = (i, i+1)
      else:
        if pairs[pair][-1] != i:
          return True
    return False

  def has_double_char_divided(s):
    for i in range(len(s)-2):
      if s[i:i+3] == s[i:i+3][::-1]:
        return True
    return False

  total = 0
  for s in lines:
    if has_double_pair(s) and has_double_char_divided(s):
      total += 1

  print(total)


if __name__ == "__main__":
  main()
