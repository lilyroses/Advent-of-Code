# Solution 1 - Advent of Code 2022, Day 2
INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():

  LOSE = 0
  TIE = 3
  WIN = 6

  MOVES = {
    "X": 1,
    "Y": 2,
    "Z": 3
  }

  OUTCOMES = {
    "AX": TIE,
    "AY": WIN,
    "AZ": LOSE,
    "BX": LOSE,
    "BY": TIE,
    "BZ": WIN,
    "CX": WIN,
    "CY": LOSE,
    "CZ": TIE
  }

  score = 0
  for line in lines:
    opp, player = line.split()
    score += MOVES[player] + OUTCOMES[f"{opp}{player}"]

  print(score)

if __name__ == "__main__":
  main()
