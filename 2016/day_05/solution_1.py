# Solution 1 - Advent of Code 2016, Day 5
import json
from hashlib import md5


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
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


if __name__ == "__main__":
    main()
