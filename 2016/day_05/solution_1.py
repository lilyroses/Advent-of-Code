# Solution 1 - Advent of Code 2016, Day 5
<<<<<<< HEAD
=======
import json
>>>>>>> c6569d7ae690c569d4242eac22cc72692afad02a
from hashlib import md5


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
<<<<<<< HEAD
  i = 0
  door_id = lines[0]

  pwd = ""
  while True:
    s = door_id+str(i)
    hash = md5(s.encode()).hexdigest()

    if hash.startswith("00000"):
      pwd += hash[5]
      print(f"\nFOUND HASH #{len(pwd)}\n")

    if len(pwd) == 8:
      break

    i += 1

  print(pwd)
=======
    """Solution for Advent of Code, 2016 Day 5 (Part I).
    
    Takes a 
    """
    door_id = lines[0]
    i = 0
    str_to_find = "00000"
    char_idx = 5

    pwd_len = 8
    pwd = ""

    while True:
        s = f"{door_id}{i}"
        hash = md5(s.encode("utf-8")).hexdigest()


        if hash.startswith(str_to_find):
            char = hash[char_idx]
            pwd += char

            print(f"CHAR FOUND: {char}")

        if len(pwd) == pwd_len:
            print(f"\n\nPASSWORD FOUND: {pwd}")
            break

        i += 1

    with open(hash_map_file_name, "w") as j:
        json.dump(hash_map, j, indent=4)
>>>>>>> c6569d7ae690c569d4242eac22cc72692afad02a


if __name__ == "__main__":
    main()
