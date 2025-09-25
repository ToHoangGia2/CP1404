
MINIMUM_PASSWORD_LENGTH = 8

def main():
    """get and check password then print afterisks according to password length"""
    entered_password = get_password()
    print_afterisks(entered_password)


def print_afterisks(entered_password):
    """print afterisks according to input length"""
    print("*" * len(entered_password))


def get_password():
    """get and check password return when the password is valid"""
    entered_password = input("Enter a password: ")
    while len(entered_password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Enter a password that is longer than {MINIMUM_PASSWORD_LENGTH} characters")
        entered_password = input("Enter a password: ")
    return entered_password


main()