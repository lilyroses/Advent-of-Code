# Solution 2 - Advent of Code 2016, Day 5
import json
from hashlib import md5


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():

    door_id = lines[0]
    i = 0
    str_to_find = "00000"
    char_idx = 6
    char_pos_idx = 5

    pwd_len = 8
    pwd_chars = ["" for i in range(pwd_len)]
    
    found_positions = []

    # while True:
    #     s = f"{door_id}{i}"
    #     hash = md5(s.encode("utf-8")).hexdigest()

    #     if hash.startswith(str_to_find):
    #         char = hash[char_idx]
    #         pos = hash[char_pos_idx]

    #         if pos not in found_positions and pos in range(pwd_len):
    #             pwd_chars[pos] = char

    #             print(f"CHAR FOUND: {char}")

    #     if len(pwd_chars) == pwd_len:
    #         pwd = "".join(pwd_chars)
    #         print(f"\n\nPASSWORD FOUND: {pwd}")
    #         break

    #     i += 1

    for hashed in hash_map.values():
        char = hashed[char_idx]
        pos = hashed[char_pos_idx]
        if pos not in found_positions and pos in range(pwd_len):
            pwd_chars[pos] = char

    if len(found_positions) != pwd_len:
        print("Password not finished", pwd_chars)

    else:
        print("".join(pwd_chars))


if __name__ == "__main__":
    main()
