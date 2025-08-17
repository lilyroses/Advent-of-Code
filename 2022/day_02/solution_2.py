# Solution 2 - Advent of Code 2022, Day 2

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  score = 0
  for line in lines:
    opp, player = line.split()
    if player == "X":
      if opp == "A":
        # lose to rock
        score += 3
      elif opp == "B":
        # lose to paper
        score += 1
      elif opp == "C":
        # lose to scissors
        score += 2
    elif player == "Y":
      score += 3
      if opp == "A":
        # tie to rock
        score += 1
      elif opp == "B":
        # tie to paper
        score += 2
      elif opp == "C":
        # tie to scissors
        score += 3
    elif player == "Z":
      score += 6
      if opp == "A":
        # win to rock
        score += 2
      elif opp == "B":
        # win to paper
        score += 3
      elif opp == "C":
        # win to scissors
        score += 1
  print(score)


if __name__ == "__main__":
  main()
