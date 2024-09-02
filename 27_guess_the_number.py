import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your Guess\n")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > highest_num or guess < lowest_num:
            print("The Number is out of Range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Too High, Try again !")
        elif guess < answer:
            print("Too Low, Try again !")
        else:
            print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
            print(f"CORRECT!, The answer is {answer}")
            print(f"Number of guesses are : {guesses}")
            is_running = False

    else:
        print("Enter the Valid Number")
        print(f"Select a number between {lowest_num} and {highest_num}")
