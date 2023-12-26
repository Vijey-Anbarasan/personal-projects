import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    guessed_number = None

    print("Welcome to the Number Guessing Game!")

    while guessed_number != target_number:
        guessed_number = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        if guessed_number < target_number:
            print("Too low! Try again.")
        elif guessed_number > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")

number_guessing_game()
