import random

playerguess = input("Enter a number: ")
guesses = 0
if playerguess.isdigit():
    playerguess = int(playerguess)

    if playerguess <= 0:
        print("Please type a number higher than 0")
    else:
        rand_number = random.randint(1, 15)
        print("Random number generated")
else:
    print("Please type a valid number")

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number')
        continue

    if user_guess == rand_number:
        print("You got it right!")
        break
    else:
        if user_guess > rand_number:
            print("The number is lower")
        else:
            print("The number is higher")

print("You got it in", guesses, "guesses")