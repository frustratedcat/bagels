import random
import os


def main():
    introduction()
    evaluate_guess()


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
        player_choice = int(input("Guess a number from 0 to 9\n> "))
        player_guesses.append(player_choice)
    return player_guesses


def evaluate_guess():
    guess_number = 1
    result = []

    random_nums = get_random_numbers()
    print(random_nums)

    while guess_number <= 10:
        print(f"Guess #{guess_number}")

        player_guess = get_player_guess()

        for i in player_guess:
            if i in random_nums:
                if player_guess.index(i) == random_nums.index(i):
                    result.append("Fermi")
                else:
                    result.append("Pico")

        if result == ["Fermi", "Fermi", "Fermi"]:
            print("You win!")
            break
        elif result == []:
            print("Bagels")
        elif "Pico" in result and "Fermi" in result:
            print("Fermi Pico")
        elif "Pico" in result:
            print("Pico")
        elif "Fermi" in result:
            print("Fermi")

        if guess_number == 10:
            print("That's 10 guesses, you lose!")
            break
        else:
            guess_number += 1
            result = []


if __name__ == "__main__":
    main()
