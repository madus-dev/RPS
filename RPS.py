import random
computer = 0
player = input('')

while True:
    rando = random.randrange(1,4)
    if rando == 1:
        computer = "rock"
    if rando == 2:
        computer = "paper"
    else:
        computer = "scissors"




    if player == computer:
        print("Tie game")
        break
    if player == "rock" and computer == "scissors":
        print("You're winner")
        break
    if player == "rock" and computer == "paper":
        print("Youre' Loser")
        break
    if player == "paper" and computer == "rock":
        print("You're Winner")
        break
    if player == "paper" and computer == "scissors":
        print("You're Loser")
        break
    if player == "scissors" and computer == "rock":
        print("You're Loser")
        break
    if player == "scissors" and computer == "paper":
        print("Youre Winner")
        break
    if player != "rock" or "paper" or "scissors":
        print("L2P Scrub")
        break
