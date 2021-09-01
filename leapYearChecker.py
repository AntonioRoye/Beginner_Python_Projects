def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


while True:
    choice = int(input("Enter a year to check if it is a leap year: "))

    if isLeapYear(choice):
        print("Yes! This is a leap year!")
    else:
        print("No! This is not a leap year!")
