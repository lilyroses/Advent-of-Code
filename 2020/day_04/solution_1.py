# Solution 1 - Advent of Code 2020, Day 4

INPUT_FILE = "input.txt"
INPUT_FILE = "input2.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    fields = "byr iyr eyr hgt hcl ecl pid cid".split()
    req_fields = fields[:-1]

    passports = []
    
    passport = []
    for line in lines:
        if line == "":
            passports.append(passport)
            passport = []
        else:
            items = line.split(" ")
            data = [item.split(':') for item in items]
            for item in data:
                passport.append(item)
    
    passports.append(passport)

    total = 0
    for passport in passports:
        passport in passport 
        ks = set([k for k, v in passport if k != "cid"])
        if len(ks) == len(req_fields):
            total += 1
    print(total)
    print(len(passports))

  


if __name__ == "__main__":
    main()
