import sqlite3


def printMenu():
    # Prints contact book menu
    print(
        """
    1. List contacts
    2. Create contacts
    3. Update contacts
    4. Delete contact
    5. View contact info
    6. Exit
        """
    )


def getFirstName():
    while True:
        firstName = input("Enter first name: ").strip()
        print(firstName)
        if firstName.replace(" ", "").isalpha():
            return firstName
        else:
            print("Enter a valid name!")


def getLastName():
    while True:
        lastName = input("Enter last name: ").strip()
        if lastName.replace(" ", "").isalpha():
            return lastName
        else:
            print("Enter a valid name!")


def getNumber():
    number = input("Enter phone number: ").strip()
    if number.isdigit():
        return number
    else:
        print("Enter a valid number!")


# Create Table if it doesn't exist
connection = sqlite3.connect("contacts.db")
crsr = connection.cursor()
createTable = """ CREATE TABLE IF NOT EXISTS Contacts (
    FIRSTNAME TEXT NOT NULL,
    LASTNAME TEXT NOT NULL,
    NUMBER INTEGER NOT NULL,
    PRIMARY KEY(FIRSTNAME, LASTNAME)
);"""
crsr.execute(createTable)
connection.commit()
connection.close()


while True:
    printMenu()
    choice = input("Enter option: ")

    if choice == 1:
        connection = sqlite3.connect("contacts.db")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM Contacts")
        ans = crsr.fetchall()
        print(ans)
        connection.close()
    elif choice == 2:
        connection = sqlite3.connect("contacts.db")
        crsr = connection.cursor()
        firstName = getFirstName()
        lastName = getLastName()
        number = getNumber()
        crsr.execute("INSERT INTO Contacts VALUES (\"{0}\", \"{1}\", {2});".format(
            firstName, lastName, number))
        connection.commit()
        connection.close()
    elif choice == 3:
        connection = sqlite3.connect("contacts.db")
        crsr = connection.cursor()

        firstName = getFirstName()
        lastName = getLastName()
        print("\nEnter updated info")
        newFirstName = getFirstName()
        newLastName = getLastName()
        newNumber = getNumber()

        crsr.execute("UPDATE Contacts SET FIRSTNAME = \"{0}\", LASTNAME = \"{1}\", NUMBER = {2} WHERE FIRSTNAME = \"{3}\" AND LASTNAME = \"{4}\";".format(
            newFirstName, newLastName, newNumber, firstName, lastName))
        connection.commit()
        connection.close()
    elif choice == 4:
        connection = sqlite3.connect("contacts.db")
        crsr = connection.cursor()

        firstName = getFirstName()
        lastName = getLastName()
        crsr.execute("DELETE FROM Contacts WHERE FIRSTNAME = \"{0}\" AND LASTNAME = \"{1}\"".format(
            firstName, lastName))
        connection.commit()
        connection.close()
    elif choice == 5:
        connection = sqlite3.connect("contacts.db")
        crsr = connection.cursor()

        firstName = getFirstName()
        lastName = getLastName()
        crsr.execute(
            "SELECT * FROM Contacts WHERE FIRSTNAME = \"{0}\" AND LASTNAME = \"{1}\"".format(firstName, lastName))
        ans = crsr.fetchall()
        print(ans)
        connection.commit()
        connection.close()
    elif choice == 6:
        print("Goodbye!\n")
        exit()
    else:
        print("Invalid choice. Try again.")
