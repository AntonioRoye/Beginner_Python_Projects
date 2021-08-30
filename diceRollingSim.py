import random

def printDie(num):
    if num == 1:
        print(" ", end="")
        print("-" * 10)
        print("|         |")
        print("|    *    |")
        print("|         |")
        print("-" * 10)
    elif num == 2:
        print(" ", end="")
        print("-" * 10)
        print("|    *    |")
        print("|         |")
        print("|    *    |")
        print("-" * 10)
    elif num == 3:
        print(" ", end="")
        print("-" * 10)
        print("| *       |")
        print("|    *    |")
        print("|       * |")
        print("-" * 10)
    elif num == 4:
        print(" ", end="")
        print("-" * 10)
        print("| *     * |")
        print("|         |")
        print("| *     * |")
        print("-" * 10)
    elif num == 5:
        print(" ", end="")
        print("-" * 10)
        print("| *     * |")
        print("|    *    |")
        print("| *     * |")
        print("-" * 10)
    else:
        print(" ", end="")
        print("-" * 10)
        print("| *     * |")
        print("| *     * |")
        print("| *     * |")
        print("-" * 10)

while True:
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    
    printDie(num1)
    printDie(num2)


    answer = int(input("Continue rolling? Press 1 to continue, 0 to exit:"))
    if answer == 0:
        exit()
    

    