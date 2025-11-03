# Solution 2 - Advent of Code 2016, Day 4
from string import ascii_lowercase as letters


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  def rotation_cipher(s, rot, charset=letters):
    nums = list(range(len(letters)))
#    char_map = dict(zip(letters, nums))
    num_map = dict(zip(nums, letters))

    rot_vals = [num+sector_id if num+sector_id <= nums[-1]
                else (num+sector_id) % len(letters)
                for num in nums]
    rot_chars = [num_map[val] for val in rot_vals]
    rot_map = dict(zip(letters, rot_chars))

    rs = ""
    for char in s:
      if char in letters:
        rs += rot_map[char]
      else:
        rs += char
    return rs


  for line in lines:
    items = line.split("[")[0].split("-")
    msg = " ".join(items[:-1])
    sector_id = int(items[-1])

    rs = rotation_cipher(msg, sector_id)
#    if "north" in rs:
#      print(rs, sector_id)
    print(rs, sector_id)


if __name__ == "__main__":
  main()
