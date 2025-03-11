import random

print("Welcome to this game of Rock Paper Scissors!\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerPick = int(input(f"Pick a number:\n Rock 1: {rock} Paper 2: {paper} or Scissors 3: {scissors}\n:"))

cpuPick = random.randint(1, 3)

if cpuPick == 1:
    if playerPick == 2:
        print(f"Paper: {paper} beats \nRock: {rock}")
        print("Player Wins")
    elif playerPick == 1:
        print(f"Rock: {rock} draws with \nRock: {rock}")
        print("Game ends in a Draw !")
    elif playerPick == 3:
        print(f"Scissors: {scissors} loses against \nRock: {rock}")
        print("Cpu Wins")
if cpuPick == 2:
    if playerPick == 3:
        print(f"Scissors: {scissors} beats \nPaper: {paper}")
        print("Player Wins")
    elif playerPick == 2:
        print(f"Paper: {paper} draws with \nPaper: {paper}")
        print("Game ends in a Draw !")
    elif playerPick == 1:
        print(f"Rock: {rock} loses against \nPaper: {paper}")
        print("Cpu Wins")
if cpuPick == 3:
    if playerPick == 1:
        print(f"Rock: {rock} beats \nScissors: {scissors}")
        print("Player Wins")
    if playerPick == 3:
        print(f"Scissors: {scissors} draws with \nScissors: {scissors}")
        print("Game ends in a Draw !")
    elif playerPick == 2:
        print(f"Paper: {paper} loses against \nScissors: {scissors}")
        print("Cpu Wins")