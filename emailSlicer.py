email = input("What is your email?: ")

username = email[:email.index("@")]

domain = email[email.index("@")+1:]

print("The username is " + username)

print("The domain is " + domain)


