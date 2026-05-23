# Solution 2 - Advent of Code 2019, Day 3

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    line_instrs = [line.split(',') for line in lines]


    def get_pts(line_instr):
        x, y = 0, 0

        pts = []
        for instr in line_instr:
            d = instr[0]
            val = int(instr[1:])

            if d == 'R':
                for dx in range(x+xi, x+xi+val*xi, xi):
                    for dy in range(y+yi, y+yi+val*yi, yi):
                        pts.append((dx, y))
                x = dx
                y = dy

            elif d == 'U':
                xi, yi = (0, 1)
                for dy in range(y+yi, y+yi+val*yi, yi):
                        pts.append((x, dy))
                y = dy

            elif d == 'L':
                xi, yi = (-1, 0)
                for dx in range(x+xi,, x+xi+val*xi, xi):
                    pts.append((dx, y))
                x = dx

            elif d == 'D':
                xi, yi = (0, -1)
                for dy in range(y+yi, y+yi+val*yi, yi):
                    pts.append((x, dy))
                y = dy

        return pts

    pts1 = get_pts(line_instrs[0])
    pts2 = get_pts(line_instrs[1])
    ipts = set(pts1) & set(pts2)

    ts = []
    for ipt in ipts:
        i1 = pts1.index(ipt) + 1
        i2 = pts2.index(ipt) + 1
        ts.append(i1 + i2)

    print(min(ts))


if __name__ == "__main__":
    main()
