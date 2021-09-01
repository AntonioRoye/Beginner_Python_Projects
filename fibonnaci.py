
def displayFib(num):
    fib = [0,1]
    
    for x in range(num-2):
        fib.append((fib[x] + fib[x+1]))

    print(fib)



choice = int(input("How many fibonacci numbers to print: "))
displayFib(choice)
