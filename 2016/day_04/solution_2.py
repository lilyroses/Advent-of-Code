# Solution 2 - Advent of Code 2016, Day 4
from string import ascii_lowercase as letters


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
<<<<<<< HEAD

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
=======
    LETTERS = list(letters)
    NUMS = list(range(0, len(LETTERS)))
    LETTER_MAP = dict(zip(LETTERS, NUMS))
    MAP_LETTER = dict(zip(NUMS, LETTERS))

    for line in lines:
        room_id = line.split("-")
        s = "-".join(room_id[:-1])
        sector_id = int(room_id[-1].split("[")[0])

        new_letters = ""
    
        for char in s:
            if char not in LETTERS:
                new_letters += char
            else:
                original_val = LETTER_MAP[char]
                new_val = (original_val + sector_id) % len(LETTERS)
                new_char = MAP_LETTER[new_val]
                new_letters += new_char
        if "north" in new_letters:
            print(new_letters, sector_id)
    
>>>>>>> c6569d7ae690c569d4242eac22cc72692afad02a


if __name__ == "__main__":
    main()
