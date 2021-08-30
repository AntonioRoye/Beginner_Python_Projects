import random
import math

def binarySearch(num, numList, start, finish):
    if num > numList[finish] or num < numList[start]:
        return None

    mid = finish - math.floor((finish-start)/2)

    if num == numList[mid]:
        return mid
    elif num > numList[mid]:
        return binarySearch(num, numList, mid, finish)
    else:
        return binarySearch(num, numList, start, mid-1)



numList = sorted(list(set([random.randint(1,100) for i in range(1,101)])))
print(numList)

while True:

    num = int(input("Enter a number to check if it is in the list: "))

    ans = binarySearch(num, numList, 0, len(numList)-1)

    if ans != None:
        print("The index of the num is: " + str(ans))
    else:
        print("The number is not in the list")
    


