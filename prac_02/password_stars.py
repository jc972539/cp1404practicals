"""Password checking program"""

def main():
    """Run program"""
    password_length = 8
    get_password(password_length)
    print_asterisks(password_length)

def print_asterisks(password_length):
    """Print asterisks"""
    print("*" * password_length)

def get_password(password_length):
    """Get input with error-checking"""
    password = input("Enter password: ")
    while len(password) < password_length:
        print("Password does not meet the minimum requirements")
        password = input("Enter password: ")

main()