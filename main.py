import random
import os


def main():
    introduction()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def introduction():
    print("""Welcome to Bagels, a deductive logic game!

You will be given a 3-digit number of which you will have 10 tries to guess.
        
Here are the rules:

When I say Pico, that means you guessed a correct digit in the wrong place.
When I say Fermi, that means you guessed a correct digit in the correct place.
When I say Bagels, that means your guess did not match any digits.""")


if __name__ == "__main__":
    main()
