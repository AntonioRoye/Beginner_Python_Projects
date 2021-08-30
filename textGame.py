print("\nWelcome. There is so much to explore!\n")


moves = 0

currentLocation = "start"

def printKitchen():
    print("-" * 7, end = " ")
    print("|", end = " ")
    print(" " * 3, end = " ")
    print("|", end = " ")
    print("-" * 7, end = " ")
    print("\n" * 2)
    print("You are now in the Kitchen.\nThe walls are blue and \nthe floor is green.")
    print("\n" * 2)
    print("-" * 7, end = " ")
    print("|", end = " ")
    print(" " * 3, end = " ")
    print("|", end = " ")
    print("-" * 7, end = " ")

def printBathroom():
    print("-" * 25)
    print("\n" * 2)
    print("You are now in the bathroom.\nThe walls are red and \nthe floor is black.")
    print("\n" * 2)
    print("-" * 7, end = " ")
    print("|", end = " ")
    print(" " * 3, end = " ")
    print("|", end = " ")
    print("-" * 7, end = " ")

def printStart():
    print("-" * 20)
    print("\n" * 2)
    print("Starting Point")
    print("\n" * 2)
    print("-" * 20)


printStart()

while True:
    answer = input("\nEnter a direction to move in (left, right, up, or down). Type exit to leave: ")
    print(" ")

    if answer == 'exit':
        print("Goodbye. Hope you had fun!")
        exit()

    if currentLocation == 'start':
        if answer == 'right':
            moves += 1
            currentLocation = "kitchen"
            printKitchen()
            print("\nYou have made " + str(moves) + " moves.\n")
        else:
            print("You cant move in that direction! Try again.")
    elif currentLocation == 'kitchen':
        if answer == 'up':
            moves += 1
            currentLocation = "bathroom"
            printBathroom()
            print("\nYou have made " + str(moves) + " moves.\n")
        elif answer == 'left':
            moves += 1
            currentLocation = "start"
            printStart()
            print("\nYou have made " + str(moves) + " moves.\n")
        else:
            print("That part of the house is currently under construction! Try again.")
    elif currentLocation == 'bathroom':
        if answer == 'down':
            moves += 1
            currentLocation = "kitchen"
            printKitchen()
            print("\nYou have made " + str(moves) + " moves.\n")
        else:
            print("You cant move in that direction! Try again.")
