# Solution 1 - Advent of Code 2021, Day 3
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    n = len(lines[0])
    gamma = ""

    for i in range(n):
        ones = 0
        zeros = 0
        for line in lines:
            if line[i] == "1":
                ones += 1
            elif line[i] == "0":
                zeros += 1
            else:
                print(f"Error: unknown value {line[i]}")
        if ones > zeros:
            gamma += "1"
        elif zeros > ones:
            gamma += "0"

    epsilon = ""
    for bit in gamma:
        if bit == "1":
            epsilon += "0"
        elif bit == "0":
            epsilon += "1"

    v1 = int(gamma, 2)
    v2 = int(epsilon, 2)
    res = v1 * v2
    print(res)
          

if __name__ == "__main__":
    main()
