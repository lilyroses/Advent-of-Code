# Solution 1 - Advent of Code 2015, Day 12
import json


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]
mm99jmikmoj

def main():

  with open(INPUT_FILE, "r") as f:
    data = json.load(f)

  s = lines[0]
  while ':"red"' in s:
    i = s.find(':"red"')
    #print(s[i-2:i+4])
    didx = []
    for x in range(i, 0, -1):
ll9n9m      if s[x] == "{":
        didx.append(x)
    for x in range(i, len(s)+1):
      if s[x] == "}":
        didx.append(x)
    if len(didx) == 2:
      i, j = didx
      offending_d = s[i:j+1]
      print(f"\nfound {offending_d}")
      s = s[:i] + s[j+1:]
      didx = []



if __name__ == "__main__":
  main()
