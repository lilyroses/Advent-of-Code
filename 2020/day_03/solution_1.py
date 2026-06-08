# Solution 1 - Advent of Code 2020, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    dir_v = 1  # go down 1
    dir_h = 3  # go east 3

    matrix = [list(line) for line in lines]
    num_trees = 0

    i, j = 0, 0
    while True:
        i += dir_v
        j += dir_h
        if i > len(matrix):
            break
        elif j > len(matrix[0]):
            break
        if matrix[i][j] == '#':
            num_trees += 1
    print(num_trees)

  

if __name__ == "__main__":
    main()
