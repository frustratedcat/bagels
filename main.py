import random
import os


def main():
    introduction()
    print(get_random_numbers())
    print(get_player_guess())


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def introduction():
    print("""Welcome to Bagels, a deductive logic game!

You will be given a 3-digit number of which you will have 10 tries to guess.
        
Here are the rules:

When I say Pico, that means you guessed a correct digit in the wrong place.
When I say Fermi, that means you guessed a correct digit in the correct place.
When I say Bagels, that means your guess did not match any digits.""")


def get_random_numbers():
    random_number = []
    for i in range(3):
        random_number.append(random.randint(0, 9))
    return random_number


def get_player_guess():
    player_guesses = []
    for i in range(3):
        player_choice = int(input("Guess a number from 0 to 9"))
        player_guesses.append(player_choice)
    return player_guesses


if __name__ == "__main__":
    main()
