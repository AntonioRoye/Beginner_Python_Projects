import random

num = random.randint(0,50)
numOfGuesses = 9

while numOfGuesses > 0:
    answer = int(input("Enter an integer between 0 and 50: "))

    if answer > num:
        numOfGuesses -= 1
        print("Guess is too high! Guess lower. You have " + str(numOfGuesses) + " tries left.\n")
    elif answer < num:
        numOfGuesses -= 1
        print("Guess is too low! Guess higher. You have " + str(numOfGuesses) + " tries left.\n")
    else:
        numOfGuesses -= 1
        print("You guessed the correct number! You had " + str(numOfGuesses) + " tries left.\n")
        exit()
    

print("You lost! The number was " + num + ". Try again")


