import random

number = random.randint(1, 101)
guess = 0

while guess != number:
    guess = int(input("Please enter your guess from 1 to 100: "))
    if guess < number:
        print("Guess higher!")
    elif guess > number:
        print("Guess lower!")
    else:
        print("You won!")
