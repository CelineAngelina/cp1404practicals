"""
Emails
Estimate: 60 minutes
Actual:   73 minutes
"""
def main():
    """Prompt the user to enter email addresses, extract and confirm names, then display their name and email."""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        formatted_name = extract_name_from_email(email)

        check_name = input(f"Is your name {formatted_name}? (Y/n) ").lower()

        if check_name != "no" and check_name != "n":
            email_to_name[email] = formatted_name
        else:
            amend_name = input("Name: ").title()
            email_to_name[email] = amend_name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    """Extract and format user's name from the given email address."""
    username = email.split("@")
    name = username[0].split(".")
    return " ".join(name).title()

main()