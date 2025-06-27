# Solution 1 - Advent of Code 2015, Day 11
from string import ascii_lowercase

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  nums = [n for n in range(len(ascii_lowercase))]
  char_map = dict(zip(ascii_lowercase, nums))

  passwd = lines[0]
  passwd_map = [char_map[char] for char in passwd]

  def has_char_straight(passwd):
    for i in range(len(passwd)-2):
      if passwd[i:i+3] in ascii_lowercase:
        return True
    return False

  def devoid_illegal_char(passwd):
    illegal_chars = ["i", "l", "o"]
    for illegal_char in illegal_chars:
      if illegal_char in passwd:
        return False
    return True

  def has_two_pairs(passwd):
    pairs = []
    for i in range(len(passwd)-1):
      pair = passwd[i:i+2]
      if pair == pair[::-1]:
        idxs = [i, i+1]
        if not pairs:
          pairs.append(idxs)
        else:
          if pairs[-1][-1] != idxs[0]:
            pairs.append(idxs)
    return len(pairs) >= 2


  print(has_two_pairs("andfrgjdddss"))


if __name__ == "__main__":
  main()
