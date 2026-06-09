# Solution 1 - Advent of Code 2020, Day 4
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():

    def byr_valid(byr):
        return 2002 >= int(byr) >= 1920
    

    def iyr_valid(iyr):
        return 2020 >= int(iyr) >= 2010


    def eyr_valid(eyr):
        return 2030 >= int(eyr) >= 2020
    

    def hgt_valid(hgt):
        metric = hgt[-2:]
        val = hgt[:-2]
        if metric == "in":
            return 76 >= int(val) >= 59
        elif metric == "cm":
            return 193 >= int(val) >= 150
        else:
            return False


    def hcl_valid(hcl):
        CHARSET = list("abcdef") + list(range(10))
        if hcl[0] == "#" and len(hcl) == 7:
            for char in hcl[1:]:
                if char not in CHARSET:
                    return False    
            return True
        return False


    def ecl_valid(ecl):
        ecl_values = "amb blu brn gry grn hzl oth".split()
        return ecl in ecl_values
    

    def pid_valid(pid):
        digits = list("0123456789")
        return len(pid) == 9 and set(pid).issubset(digits)


    fields = "byr iyr eyr hgt hcl ecl pid cid".split()
    req_fields = fields[:-1]

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
