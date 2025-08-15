# Solution 2 - Advent of Code 2015, Day 19
from collections import defaultdict as dd


INPUT_FILE = "input.txt"
#INPUT_FILE = "test_input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  all_new_seqs = set()
  replacements = dd(list)
  orig_s = lines[-1]
  orig_seqs = list(replacements.keys())

  for line in lines:
    if "=>" in line:
      items = line.split()
      start_molecule = items[0]
      end_molecule = items[-1]
      replacements[start_molecule].append(end_molecule)


  def replace_substr(old_s, new_s):
    new_seqs = []
    # substrs to replace are padded with space chars
    spaced_seq = orig_s.replace(old_s, f" {old_s} ")
    orig_items = spaced_seq.split()
    idxs = [i for i, item in enumerate(orig_items)
            if item == old_s]

    for idx in idxs:
      items = orig_items[:]
      items[idx] = new_s
      new_seq = "".join(items)
      new_seqs.append(new_seq)

    return new_seqs

  old_substr = "e"
  new_substrs = replacements[old_substr]
  


if __name__ == "__main__":
  main()
