# Solution 1 - Advent of Code 2019, Day 2

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
#    lines = ["1,0,0,0,99"]
#    lines = ["2,3,0,3,99"]
#    lines = ["2,4,4,5,99,0"]
#    lines = ["1,1,1,4,99,5,6,0,99"]
    vals = [int(n) for n in lines[0].split(',')]

    i = 0

    vals[1] = 12
    vals[2] = 2

    print(f"\ni: {i}")
    print(f"\t- vals: {vals}")

    while True:

#        if i >= len(vals)-4:
#            print(f"\nEXIT\n")
#            print(f"\nvals[0]: {vals[0]}\n")
#            return

        opcode = vals[i]

        if opcode == 99:
            print(f"\nEXIT CODE {opcode}\n")
            print(f"\nvals[0]: {vals[0]}\n")
            return

            return

        v1_idx = vals[i+1]
        v2_idx = vals[i+2]
        res_idx = vals[i+3]

        v1 = vals[v1_idx]
        v2 = vals[v2_idx]

        if opcode == 1:
            s = '+'
            res = v1 + v2

        elif opcode == 2:
            s = '*'
            res = v1 * v2

        else:
            print(f"Error: unknown opcode '{opcode}'")
            return

        print(f"\nOPCODE: {opcode} [{s}]")
        print(f"\t- v1:   {v1} [idx: {v1_idx}]")
        print(f"\t- v2:   {v2} [idx: {v2_idx}]")
        print(f"\t- res:  {res} [{v1} {s} {v2}] -> idx [{res_idx}]")

        vals[res_idx] = res
        print(f"\t- vals: {vals}")

        i += 4

        if i+3 >= len(vals):
            print(f"\nEXIT CODE {opcode}\n")
            print(f"\nvals[0]: {vals[0]}\n")
            return


if __name__ == "__main__":
    main()

