import re

password = input("Enter password: ")

if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{8,}$", password):
    print("Valid password")
else:
    print("Invalid password")