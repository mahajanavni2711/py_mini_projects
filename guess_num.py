from random import randint

EASY_LEVEL_TURNS = 7
MODERATE_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 3

# logo = """
#
# ____ _  _ ____ ____ ____    ___ _  _ ____    _  _ _  _ _  _ ___  ____ ____
# | __ |  | |___ [__  [__      |  |__| |___    |\ | |  | |\/| |__] |___ |__/
# |__] |__| |___ ___] ___]     |  |  | |___    | \| |__| |  | |__] |___ |  \

# """
# print(logo)


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The number is {actual_answer}")


def set_difficulty():
    globals()
    level = input("Choose the level of difficulty: Type 'easy' or "
                  "'moderate' or 'hard'").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "moderate":
        return MODERATE_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number guessing game")
    print("I am thinking of the number between 1 and 50")
    answer = randint(1, 50)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You are out of guesses. You lose!")
            print(f"Pssst , the correct answer is {answer}")

            return
        elif guess != answer:
            print("Guess again")


game()