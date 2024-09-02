import random

options = ("rock", "paper", "scissor")
playing = True

while playing:
    player = None
    computer = random.choice(options)

    player = input("Enter a choice (rock, paper, scissor)\n")

    while player not in options:
        print("Enter the valid choice")
        player = input("Enter a choice (rock, paper, scissor)\n")

    print("---------------------------------------------")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    print("---------------------------------------------")
    if player == computer:
        print("Its a TIE!!")
    elif player == "rock" and computer == "scissor":
        print("You WIN! 🥳")
    elif player == "scissor" and computer == "paper":
        print("You WIN! 🥳")
    elif player == "paper" and computer == "rock":
        print("You WIN! 🥳")
    else:
        print("You Lose! 😢")

    if not input("Play again ? (y/n)\n").lower() == "y":
        playing = False

print("Thank you for Playing")
