import random

def isChar(string):
    #Checks if input is a char and alphanumeric
    if len(string) == 1 and string.isalpha():
        return True
    else:
        return False

words = ["potato", "orange", "red", "blue", "extravaganza"]

maxNumOfGuesses = 5

while True:
    wordChoice = list(words[random.randint(0,len(words)-1)])
    string = []
    for num in range(0,len(wordChoice)):
        string.append("-")
    
    while maxNumOfGuesses > 0:
        print("The word is: " + "".join(string))
        answer = input("Enter a letter: ")

        if answer in string:
            print("You already guessed that! Guess again")
            continue
        elif isChar(answer) and answer in wordChoice:
            indices = [i for i, x in enumerate(wordChoice) if x == answer]

            for num in indices:
                string[num] = answer
        else:
            maxNumOfGuesses -= 1
        
        if "".join(string) == "".join(wordChoice):
            print("You guessed the word! Congrats!")
            break
        elif maxNumOfGuesses == 0:
            print("You have no more guesses!")
            break
        else:
            print("Number of guesses left: " + str(maxNumOfGuesses))

        
    
    break

#Can add conditionals at the end of the loop to ask to continue the game or not