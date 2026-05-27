# Solution 1 - Advent of Code 2019, Day 5

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    lines = [line.strip() for line in f.readlines()]


def main():

    """
    Intcode program:

        - INSTRUCTION
          POINTER:      points to the index of the INSTRUCTION. is increased by
                        the number of values in the INSTRUCTION after the
                        INSTRUCTION ends. Not always 4.

        - POSITION:     index (i)

        - INSTRUCTION:  an OPCODE and its PARAMETERS
        
        - OPCODE:       a number that indicates which operation to perform.
                        the first value in an INSTRUCTION but the last two
                        numbers in the value. E.g. for 1002, 02 is the OPCODE
        
        - PARAMETER:    the numbers following an opcode

        - MODE:         determines if the parameters are indices (POSITION) or
                        just values (IMMEDIATE). Stored in the same value as
                        the OPCODE as the first two numbers in the value. E.g.,
                        if the value is 1002, the MODE is (from right to left)
                        0, 1, and a leading (not shown) 0.

    ===========================================================================
    
        - OPCODES:

            1 : ADD; 3 PARAMS
                [PARAM_1] : index of 1st num
                [PARAM_2] : index of 2nd num
                [PARAM_3] : index of sum

            2 : MUL; 3 PARAMS
                [PARAM_1] : index of 1st num
                [PARAM_2] : index of 2nd num
                [PARAM_3] : index of product
    
            3 : INPUT; 1 PARAM
                [PARAM_1] : INPUT index

            4 : OUTPUT; 1 PARAM
                [PARAM_1] : OUTPUT index
            
            99 : EXIT
    
    ===========================================================================

        - MODES:

            0 : POSITIONAL
                [PARAM] is a POSITION

            1 : IMMEDIATE
                [PARAM] is a value
    
    ===========================================================================

        - EXAMPLE PROGRAM: 1002,4,3,4,33
                
            [INSTR_1]: 1002,4,3,4

                - OPCODE :
                        [02] MUL

                - PARAM MODES:
                        [0] POS
                        [1] IMM
                        [0] POS

        - EXPLANATION:
        
            A B C D E
              1 0 0 2
                  * *   - [DE] OPCODE        [02] MUL  
                *       - [C]  PARAM_1 MODE  [0]  POS
              *         - [B]  PARAM_2 MODE  [1]  IMM
            *           - [A]  PARAM_3 MODE  [0]  POS

        This instruction MULTIPLIES its first 2 PARAMETERS:

            - [PARAM_1] is in POSITION mode, so the first value is at index [PARAM_1].
            - [PARAM_2] is in IMMEDIATE mode, so the second value is [PARAM_2].
            - [PARAM_3] is in POSITION mode, so the result of multiplying the first
                        and second values is stored at index [PARAM_3].

        
    """
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
            elif op == 3:
                res = v1
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
=                 return


if __name__ == "__main__":
    main()

