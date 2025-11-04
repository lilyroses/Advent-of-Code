# Solution 1 - Advent of Code 2017, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    target = int(lines[0])
    target = 13

    ring, rows, cols = 1, 1, 1
    min_val, max_val = 1, 1

    while True:
        ring += 1
        rows += 2
        cols += 2
        min_val = max_val + 1
        max_val = rows*cols

        steps_to_mid = rows//2

        # FIND LEFT COL

        # FIND BOTTOM ROW

        if target in range(min_val, max_val+1):

            # CORNERS
            bottom_right = max_val
            top_right = min_val + (rows-2)
            top_left = top_right + (cols-1)
            bottom_left = top_left + (rows-1)
            CORNERS = [[top_left, top_right],[bottom_left, bottom_right]]
            for row in CORNERS:
                print(row)

            # RIGHT COL
            right_col = sorted(list(range(min_val, top_right+1)), reverse=True) + [max_val]

            # FIND TOP ROW
            top_row = sorted(list(range(top_right, top_left+1)), reverse=True)

            # FIND LEFT COL
            left_col = list(range(top_left, bottom_left+1))

            # FIND BOTTOM ROW
            bottom_row = list(range(bottom_left, max_val+1))
            
            
            print(f"TOP ROW: {top_row}")
            print(f"RIGHT COLUMN: {right_col}")
            
            print(f"\nTARGET {target:,} FOUND IN RING #{ring} ({min_val:,}-{max_val:,})") 
            print(f"STEPS TO MID: {steps_to_mid}")
            break

    # what is the relationship between rows/cols, ring, and square?
    # RING 1: 
    #   rows = 1
    #   cols = 1
    #   min, max = 1, 1
    #   square = 1 (rows*cols or (ring**2))
    # RING 2:
    #   rows = 3
    #   cols = 3
    #   min, max = 2, 9
    #   square = 9 (rows*cols or (ring+1)**2)
    # RING 3:
    #   rows = 5
    #   cols = 5
    #   min, max = 10, 25
    #   square = 25 (rows*cols or (ring+2)**2)
    square = 1

    # MID: where "1" is located, from either side (up/down or left/right) of
    # the grid
    # mid_horiz = rows//2
    # mid_vert = cols//2 




if __name__ == "__main__":
    main()
