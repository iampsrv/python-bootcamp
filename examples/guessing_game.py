import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)
max_attempts = int(input("How many attempts would you like? "))

for attempt in range(1, max_attempts + 1):
    guess = int(input("Take a guess: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempt} attempts!")
        break
else:
    print(f"Sorry, you ran out of attempts! The secret number was {secret_number}. Better luck next time!")
