# Solution 1 - Advent of Code 2019, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    line_instrs = [line.split(',') for line in lines]

    all_pts = []
    for line_instr in line_instrs:
        pts = []
        x, y = 0,0
        for instr in line_instr:
            d = instr[0]
            val = int(instr[1:])

            if d == 'U':
                for dy in range(y, y+val+1):
                    pts.append((x, dy))
                y = dy

            elif d == 'R':
                for dx in range(x, x+val+1):
                    pts.append((dx, y))
                x = dx

            elif d == 'D':
                for dy in range(y, y-val-1, -1):
                    pts.append((x, dy))
                y = dy

            elif d == 'L':
                for dx in range(x, x-val-1, -1):
                    pts.append((dx, y))
                x = dx

        all_pts.append(set(pts))

    pts1 = set(all_pts[0])
    pts2 = set(all_pts[1])
    ipts = []
    for pt in pts1:
        if pt in pts2:
            ipts.append(pt)

    ts = []
    for p in ipts:
        ts.append((abs(p[0]) + abs(p[1])))
    print(sorted(ts)[1])

if __name__ == "__main__":
    main()
