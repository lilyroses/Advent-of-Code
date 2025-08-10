# Solution 1 - Advent of Code 2015, Day 19
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


  for old_substr, new_substrs in replacements.items():
    for new_substr in new_substrs:
      new_seqs = replace_substr(old_substr, new_substr)
#      for new_seq in new_seqs:
#        if new_seq not in all_new_seqs:
#          all_new_seqs.append(new_seq)
      all_new_seqs = all_new_seqs.union(new_seqs)

  print(len(all_new_seqs))


if __name__ == "__main__":
  main()
