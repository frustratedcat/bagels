from math import asin
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


def get_random_numbers():
    rand_one = random.randint(0, 9)
    rand_two = random.randint(0, 9)
    rand_three = random.randint(0, 9)

    random_number = [rand_one, rand_two, rand_three]
    return random_number


if __name__ == "__main__":
    main()
