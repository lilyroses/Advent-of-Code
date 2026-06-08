# Solution 2 - Advent of Code 2020, Day 3
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    matrix = [list(line) for line in lines]

    dirs = [
        (1, 1),
        # (3, 1),  # already checked
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    total_trees = 237  # the answer from the previous solution; (3,1)
    for dir_h, dir_v in dirs:
        num_trees = 0
        i, j = 0, 0

        while True:
            i += dir_v
            j = (j + dir_h) % len(matrix[0])
            if i >= len(matrix):
                break
            if matrix[i][j] == '#':
                num_trees += 1

        total_trees *= num_trees
    
    print(total_trees)
  

if __name__ == "__main__":
    main()
