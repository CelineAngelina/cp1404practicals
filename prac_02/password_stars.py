MINIMUM = 10

def main():
    """Get user password and display it as asterisks."""
    user_password = get_password()
    print_asterisks(user_password)

def get_password():
    """Get user password and ensure it meets the minimum length requirement."""
    password = input("Enter your password: ")
    while len(password) < MINIMUM:
        print(f"The password need to be at least {MINIMUM} characters!")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Display password in asterisks based on the length of password entered by user."""
    print(f"Your password is {'*' * len(password)}")

main()