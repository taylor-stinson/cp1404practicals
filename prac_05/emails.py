"""
CP1404 - Practicals
Emails
"""


def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = str(input("Email: "))
    while email != "":
        name = get_name_from_email(email).title()
        confirm = str(input(f"Is your name {name}? (Y/n)")).lower()
        if confirm != "" and confirm != "y":
            name = str(input("Name: "))
        email_to_name[email] = name
        email = str(input("Email: "))
    for key, value in email_to_name.items():
        print(f"{value} ({key})")


def get_name_from_email(email):
    """Use string formatting to get name from email address"""
    name_part = email.split("@")[0]
    names = name_part.split(".")
    name = " ".join(names)
    return name


main()
