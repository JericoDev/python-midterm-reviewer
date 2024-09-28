import random

number_to_guess = random.randint(1, 10)
user_guess = None
guess_count = 0
max_guesses = 10

while guess_count < max_guesses:
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        if user_guess < 1 or user_guess > 100:
            print("Please enter a valid number between 1 and 100.")
            continue
        
        guess_count += 1
        
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You've guessed the number in {guess_count} guesses.")
            break
else:
    print(f"Sorry, you've reached the maximum number of {max_guesses} guesses. The number was {number_to_guess}.")
