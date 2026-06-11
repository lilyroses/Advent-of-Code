# Solution 2 - Advent of Code 2020, Day 4
import json


INPUT_FILE = "input2.txt"
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    digits = list("0123456789")
    chars = list("abcdef")
    hex_digits = digits + chars
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
    passports.append(sorted(passport))  # the final passport
    
    ok_passports = []
    for passport in passports:
        passport = [item for item in passport if "cid" not in item]
        if len(passport) == len(req_fields):
            ok_passport = {}
            for k, v in passport:
                ok_passport[k] = v
            ok_passports.append(dict(sorted(ok_passport.items())))


    def byr_valid(byr):
        try:
            byr = int(byr)
        except ValueError:
            return False
        return 1920 <= byr <= 2002


    def iyr_valid(iyr):
        try:
            iyr = int(iyr)
        except ValueError:
            return False
        return 2010 <= iyr <= 2020


    def eyr_valid(eyr):
        try:
            eyr = int(eyr)

        except ValueError:
            return False
        return 2020 <= eyr <= 2030


    def hgt_valid(hgt):
        hgt_val = hgt[:-2]
        hgt_m = hgt[-2:]
        try:
            hgt_val = int(hgt_val)
        except ValueError:
            return False
        if hgt_m == "cm":
            return 150 <= hgt_val <= 193
        if hgt_m == "in":
            return 59 <= hgt_val <= 76
        return False


    def hcl_valid(hcl):
        if len(hcl) != 7 or hcl[0] != "#":
            return False
        hcl_chars = hcl[1:]
        for char in hcl_chars:
            if char not in hex_digits:
                return False
        return True


    def ecl_valid(ecl):
        for ecl_val in "amb blu brn gry grn hzl oth".split():
            if ecl_val == ecl:
                return True
        return False


    def pid_valid(pid):
        if len(pid) != 9:
            return False
        for char in pid:
            if char not in "0123456789":
                return False
        return True
    

    total_valid = 0
    for passport in ok_passports:
        if set(list(passport.keys())) == set(req_fields):
            valid_data = 0

            byr = passport["byr"]
            valid_data += byr_valid(byr)

            iyr = passport["iyr"]
            valid_data += iyr_valid(iyr)

            eyr = passport["eyr"]
            valid_data += eyr_valid(eyr)

            hgt = passport["hgt"]
            valid_data += hgt_valid(hgt)
            
            hcl = passport["hcl"]
            valid_data += hcl_valid(hcl)

            ecl = passport["ecl"]
            valid_data += ecl_valid(ecl)

            pid = passport["pid"]
            valid_data += pid_valid(pid)

            if valid_data == 7:
                total_valid += 1

    print(total_valid)


if __name__ == "__main__":
    main()
