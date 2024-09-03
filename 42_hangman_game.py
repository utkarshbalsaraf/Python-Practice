import random

words = ("cat", "dog", "cow", "goat", "sheep",
         "horse", "pig", "rabbit", "chicken", "duck",
         "lion", "tiger", "elephant", "zebra", "giraffe",
         "fox", "bear", "wolf", "deer", "mouse")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\"),
               }


def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        print("---------------------------------------------")
        print("GUESS THE ANIMAL🐶 NAME OR DIE😵 (only 6 lifelines)")
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a Letter\n").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input Enter Single character")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            print("===========================================")
            print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN! 🥳")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            print("===========================================")
            print("😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵😵")
            display_man(wrong_guesses)
            print("The Correct answer was :")
            display_answer(answer)
            print("YOU LOSE! 😵")
            is_running = False


if __name__ == '__main__':
    main()
