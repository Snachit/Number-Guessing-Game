import random

number = random.randint(1,10)
guess = input("Guess a number betweem 1 and 10 :")
guess = int(guess)

if number == guess:
    print("You won!")

else :
    print("You such a loser ")