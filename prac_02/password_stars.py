password = input("Enter your password: ")
while len(password) < 10:
    print("The password need to be at least 10 characters!")
    password = input("Enter your password: ")
print(f"Your password is {"*" * len(password)}")