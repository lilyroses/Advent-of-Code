# Solution 1 - Advent of Code 2015, Day 11
from string import ascii_lowercase


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  """Password must include:
       - one increasing straight of at least 3 letters: abc, xyz
       - no i, o, or l
       - two different, non-overlapping pairs of letters: aa, zz
  """
  
  CHAR_MAP = dict(zip(ascii_lowercase, range(0,27)))
  NUM_MAP = dict(zip(range(0,27), ascii_lowercase))
  ILLEGAL_CHARS = ["i", "l", "o"]
  LEGAL_CHAR_MAP = {letter: CHAR_MAP[letter] for letter in ascii_lowercase
                    if letter not in ILLEGAL_CHARS}

  # passwd = lines[0]
  passwd  = "hxiyyaba"


  def has_char_straight(passwd):
    for i in range(len(passwd)-2):
      if passwd[i:i+3] in ascii_lowercase:
        return True
    return False


  def devoid_illegal_char(passwd):
    for illegal_char in ILLEGAL_CHARS:
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


  if not devoid_illegal_char(passwd):
    # find the first occuring illegal character and then change it, and
    # change all chars after as well
    for i, char in enumerate(passwd):
      if char in ILLEGAL_CHARS:
        break
    illegal_letter = passwd[i]
    next_letter = NUM_MAP[CHAR_MAP[illegal_letter] + 1]
    passwd = passwd[:i]
    passwd += next_letter

  return passwd
 


if __name__ == "__main__":
  print(main())
