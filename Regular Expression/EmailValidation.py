import re
email = input("Enter email address: ")

if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
    print("Valid email address")
else:
    print("Invalid email address")