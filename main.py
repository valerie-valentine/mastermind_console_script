import random
import requests
from art import game_logo, win_logo, lost_logo

# way to generate random number -> random.randint/ function; use random.org api?
# take user input -> input function
# validate user input -> raise exception?/ ask for valid input
# create and display board -> function/ print
# check guess for valid/invalid guess, winning combination
# provide a hint/feedback
# way to keep game repeating until finished -> loop
# choose level
# restart game

# create a board that has the number as a key & lists as values
# create a list of tuples


def main():
    game_over = False
    lives = 10
    level, answer = initialize_game()
    previous_guesses = []

    print(f"Test String: {answer}")

    while not game_over and lives != 0:
        print(f"You have {lives} attempts remaining.")

        guess = user_guess(level)
        correct_number, correct_location = validate_user_guess(answer, guess)

        if guess in previous_guesses:
            print("You have already guess that number.")
            continue

        previous_guesses.append(guess)

        if correct_number == 0 and correct_location == 0:
            print("All incorrect")
        else:
            print(f"{correct_number} correct number and {
                  correct_location} correct location")

        if guess == answer:
            print(win_logo)
            print(f"The answer was: {answer}")
            game_over = True
            play_again()

        lives -= 1

    if lives == 0:
        print(lost_logo)
        print(f"The correct answer was: {answer}")
        play_again()


def initialize_game():
    start_instructions()
    level_selected = choose_level()
    answer_selected = random_number(level_selected)
    return level_selected, answer_selected


def random_number(digits):
    url = f'https://www.random.org/integers/?num={
        digits}&min=0&max=9&col=1&base=10&format=plain&rnd=new'

    response = requests.get(url)

    random_number = "".join(response.text.split())
    return random_number

    # start = 10 ** (digits - 1)
    # start = 0
    # end = (10 ** digits) - 1
    # number = str(random.randint(start, end))

    # if len(number) < digits:
    #     number = number.zfill(digits)
    # return number

# check length of number if less than digits length
# pre-pend how many zeros we need to make it the correct length
# MUST REFEACTOR AND USE API!!


def user_guess(level):
    while True:
        guess = input("Make a guess: ")
        if not guess.isnumeric():
            print("Please enter a number with a numerical value.")
            continue
        if len(guess) != level:
            print(f"Please enter a number with {level} digits.")
            continue

        return guess


def validate_user_guess(answer, guess):
    correct_number = 0
    correct_location = 0
    answer_count = {}

    for num in answer:
        answer_count[num] = answer_count.get(num, 0) + 1

    for i, num in enumerate(guess):
        if num == answer[i]:
            correct_location += 1
        if num in answer_count and answer_count[num] > 0:
            correct_number += 1
            answer_count[num] -= 1

    return correct_number, correct_location


def choose_level():
    levels = {
        "easy": 4,
        "medium": 6,
        "hard": 8
    }

    while True:
        level = input(
            f"Please select a level to play (easy: {levels["easy"]} digits, medium: {levels["medium"]} digits, hard: {levels["hard"]} digits): ").lower()
        if level not in levels.keys():
            print("Error: Please enter a valid level (easy, medium, hard).")
            continue

        return levels[level]


def start_instructions():
    print(game_logo)
    print("Welcome to Mastermind!")
    print("Play against the computer and break the code to win.")
    print("A random number from 0-9 will be generated "
          "based on the level you've chosen.")
    print("You will have 10 attempts to guess the number.")
    print("Hints will be provided to help you along the way.")
    print("Good luck!")


def play_again():
    print("Would you like to play again?")
    play_again = input(
        "Enter 'yes' to play again or 'no' to quit: ").lower()
    if play_again == "yes":
        main()
    elif play_again == "no":
        print("Thanks for playing!")
    else:
        print("Please enter a valid response.")
        return play_again()


main()
