# Solution 1 - Advent of Code 2017, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    target = int(lines[0])

    ring = 1
    min_val = 1
    max_val = 1
    num_to_square = 1

    print(f"RING #{ring} ({min_val}-{max_val})")

    while True:
        ring += 1
        num_to_square += 2
        min_val = max_val + 1
        max_val = num_to_square**2

        print(f"RING #{ring} ({min_val}-{max_val})")

        if target in range(min_val, max_val+1):
            print(f"\nFOUND TARGET {target} RING #{ring}: ({min_val}-{max_val})")
            break
  

if __name__ == "__main__":
    main()
