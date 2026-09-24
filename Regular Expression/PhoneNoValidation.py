import re
phone = input("Enter phone number: ")

if re.match(r"^[0-9]{10}$", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")