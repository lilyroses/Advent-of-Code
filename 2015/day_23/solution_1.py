# Solution 1 - Advent of Code 2015, Day 23
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():
    """
    - [r]   : register (a or b). each register has a value that is initialized to
              0. the register values are updated depending on the operation
              executed.
    
    - [op]  : operation (hlf, tpl, inc, jmp, jie, jio) that determines in
    
    """
    instrs = [line.split() for line in lines]
    REGISTERS = {'a': 0, 'b': 0}
    i = 0

    while i < len(instrs):  # until i exceeds len(instrs)-1
        instr = instrs[i]
        op = instr[0]  # operation

        if op == "hlf":
            r = instr[1]
            REGISTERS[r] //= 2
            i += 1

        elif op == "tpl":
            r = instr[1]
            REGISTERS[r] *= 3
            i += 1

        elif op == "inc":
            r = instr[1]
            REGISTERS[r] += 1
            i += 1

        elif op == "jmp":
            offset = int(instr[1])
            i += offset

        elif op == "jie":
            r = instr[1][:-1]
            if REGISTERS[r] % 2 == 0:
                offset = int(instr[2])
            else:
                offset = 1
            i += offset
        
        elif op == "jio":
            r = instr[1][:-1]
            if REGISTERS[r] == 1:
                offset = int(instr[2])
            else:
                offset = 1
            i += offset
        print(f"i: [{i}]")
        print(f"\tOP: [{op}] | R: [{r}] | OFFSET: [{offset}] | A: [{REGISTERS['a']}] | B: [{REGISTERS['b']}]")

        if i >= len(instrs):
            print(REGISTERS['b'])
            return


if __name__ == "__main__":
    main()
