gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))
marital_status = input("Enter marital status (Married/Unmarried): ")

if marital_status.lower() == "married":
    print("Eligible for Insurance")

elif gender.lower() == "m" and age > 30:
    print("Eligible for Insurance")

elif gender.lower() == "f" and age > 25:
    print("Eligible for Insurance")

else:
    print("Not Eligible for Insurance")