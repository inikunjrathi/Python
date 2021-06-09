import random

chances = 0
number = random.randint(1, 9)

while chances < 5:
    guess = int(input("Guess a number (Between 1 and 9) : "))
    if guess == number:
        print("Congratulation you WON")
        break
    else:
        chances += 1

if chances == 5:
    print("You LOSE!!! The number was %d, Better luck next time" % (number))
