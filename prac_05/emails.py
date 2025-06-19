"""
Emails
Estimate: 60 minutes
Actual:    minutes
start 2:30
stop 3:28
"""

email_to_name = {}
email = input("Email: ")

while email != "":
    username = email.split("@")
    name = username[0].split(".")
    formatted_name = " ".join(name).title()

    check_name = input(f"Is your name {formatted_name}? (Y/n) ").lower()

    if check_name != "no" and check_name != "n":
        email_to_name[email] = formatted_name
    else:
        amend_name = input("Name: ")
        email_to_name[email] = amend_name
    email = input("Email: ")

print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")

