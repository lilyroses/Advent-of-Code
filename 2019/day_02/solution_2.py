# Solution 2 - Advent of Code 2019, Day 2

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():

    def run(n, v):
        m = [int(n) for n in lines[0].split(',')]
        m[1] = n
        m[2] = v

        addr = 0
        while True:
            op = m[addr]
            if op == 99:
                return m[0]


            v1 = m[m[addr+1]]
            v2 = m[m[addr+2]]
            res_idx = m[addr+3]

            if op == 1:
                res = v1 + v2
            elif op == 2:
                res = v1 * v2
            else:
                print(f"Error: unknown opcode '{op}'")
                return

            m[res_idx] = res
            addr += 4
            if addr+3 >= len(m):
                return m[0]

    for n in range(0,100):
        for v in range(0, 100):
            res = run(n, v)
            if res == 19690720:
                 ans = (n*100) + v
                 print(ans)
                 return


if __name__ == "__main__":
    main()

