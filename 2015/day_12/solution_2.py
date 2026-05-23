# Solution 1 - Advent of Code 2015, Day 12
import json


INPUT_FILE = "input.txt"
with open(INPUT_FILE, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    data = lines[0]
    j = json.loads(data)

    found_dicts = []

    while True:
        open = False
        close = False
        i = 0
        for char in data:
            if char == "{":
                open = True
                idx = i
            elif char == "}":
                if open == True:
                    close = True
                    idx2 = i
                    s = data[idx:idx2+1]
                    found_dicts.append(s)
                    data = data.replace(s, "")
            i += 1
        if i >= len(data):
            break

    for found_dict in found_dicts:
        print(found_dict, "\n\n")

            

    # for every item in list j:
        # if item is a list
            # run this function on that list
        # if item is a dict
            # 


if __name__ == "__main__":
    main()
