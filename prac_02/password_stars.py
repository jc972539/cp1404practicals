password_length = 8
password = input("Enter password: ")
while len(password) < password_length:
    print("Password does not meet the minimum requirements")
    password = input("Enter password: ")
print("*" * password_length)