# Solution 1 - Advent of Code 2015, Day 13
INPUT_FILE = "input.txt"
with open(INPUT_FILE, 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    seat_map = {}
    names = []

    for line in lines:
        items = line.split()
        name = items[0]
        val = int(items[3])
        if items[2] == "lose":
            val *= -1
        other_name = items[-1][:-1]

        if name not in seat_map:
            seat_map[name] = {}
        seat_map[name][other_name] = val

        if name not in names:
            names.append(name)
        if other_name not in names:
            names.append(other_name)

    for name in names[:-2]:
        for name2 in names[1:]:
            print(f"{name} and {name2}")


if __name__ == "__main__":
    main()
