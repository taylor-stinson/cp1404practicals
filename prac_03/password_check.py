def main():
    MINIMUM_LENGTH = 6
    password = get_password(MINIMUM_LENGTH)
    display_password(password)


def display_password(password):
    for character in password:
        print("*", end="")


def get_password(MINIMUM_LENGTH):
    password = str(input("Enter password: "))
    while len(password) < MINIMUM_LENGTH:
        print("Password must be more than {} characters".format(MINIMUM_LENGTH))
        password = str(input("Enter password: "))
    return password


main()
