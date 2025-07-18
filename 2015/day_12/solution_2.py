# Solution 1 - Advent of Code 2015, Day 12
import json


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  total = 0
  s = lines[0]
  j = json.loads(s)

  lists = []

  def parse(j):
    dicts = []
    for item in j:
      if isinstance(item, list):
        # print(f"\nLIST:\n{item}")
        parse(item)
      elif isinstance(item, dict):
        for k, v in item.items():
          if isinstance(k, list):
            parse(k)
          elif isinstance(v, list):
            parse(v)
          else:

            dicts.append(item)
    return dicts


  # parsed_dicts = []

  # while "{" in s:
  #   i = s.index("}")
  #   # from the beginning of the string to the first occurence of a closing bracket
  #   substr = s[:i+1]
  #   # the last occurence of a closing bracket within that substring (to form an innermost dict)
  #   j = substr.rindex("{")
  #   d = s[j:i+1]
  #   dicts.append(d)
  #   # remove the dict substring from the string
  #   s = s[:j] + s[i+1:]

  # for dct in dicts:
  #   # remove the arrays from the dicts
  #   while "[" in dct:
  #     i = dct.index("]")
  #     pd = dct[:i+1]
  #     j = pd.rindex("[")
  #     d = dct[j:i+1]
  #     lists.append(d)
  #     dct = dct[:j] + dct[i+1:]
  #   parsed_dicts.append(dct)


  # for s in lists:
  #   s = s.split(":")
  #   s = " ".join(s)
  #   s = s.split(",")
  #   s = " ".join(s)
  #   s = s.split("}")
  #   s = " ".join(s)
  #   s = s.split("{")
  #   s = " ".join(s)
  #   s = s.split("[")
  #   s = " ".join(s)
  #   s = s.split("]")
  #   s = " ".join(s)
  #   s = s.split()
  #   for i in s:
  #     if '"' not in i:
  #       total += int(i)

  # for s in parsed_dicts:
  #   if 'red' not in s:
  #     s = s.split(":")
  #     s = " ".join(s)
  #     s = s.split(",")
  #     s = " ".join(s)
  #     s = s.split("}")
  #     s = " ".join(s)
  #     s = s.split("{")
  #     s = " ".join(s)
  #     s = s.split("[")
  #     s = " ".join(s)
  #     s = s.split("]")
  #     s = " ".join(s)
  #     s = s.split()
  #     for i in s:
  #       if '"' not in i:
  #         total += int(i)

  dicts = parse(j)
  for item in dicts:
    print(item)


if __name__ == "__main:__":
  main()
