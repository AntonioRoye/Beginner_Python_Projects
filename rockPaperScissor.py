import random

while True:
    moves = ["rock", "paper", "scissor"]
    compChoice = moves[random.randint(0, 2)]
    choice = input("Enter rock, paper or scissor: ")

    if choice == 'rock':
        if compChoice == 'scissor':
            print("Rock beats scissor, you won!")
        elif compChoice == 'rock':
            print("Its a tie.")
        else:
            print("You lost!")
    elif choice == 'paper':
        if compChoice == 'scissor':
            print("Scissor beats paper, you lost!")
        elif compChoice == 'rock':
            print("Paper beats rock, you won!")
        else:
            print("Its a tie.")
    elif choice == 'scissor':
        if compChoice == 'scissor':
            print("Its a  tie.")
        elif compChoice == 'rock':
            print("You lost!")
        else:
            print("Scissor beats paper, you won!")
    else:
        print("That is not a valid choice")
