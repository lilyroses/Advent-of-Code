# Solution 1 - Advent of Code 2020, Day 4
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    req_fields = "byr iyr eyr hgt hcl ecl pid cid".split()[:-1]

    passports = []  # groups of lines separated by blank line
    passport = []  # the lines in a group
    for line in lines:
        if line == "":
            passports.append(passport)
            passport = []
        else:
            items = line.split(" ")
            data = [item.split(':') for item in items]
            for item in data:
                passport.append(item)
    passports.append(passport)  # the final passport

    total = 0
    for passport in passports:
        passport in passport 
        ks = set([k for k, v in passport if k != "cid"])
        if len(ks) == len(req_fields):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
