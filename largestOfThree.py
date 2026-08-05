n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
p = int(input("Enter third number: "))

if n > m and n > p:
    print("The largest number is:", n)
elif m > n and m > p:
    print("The largest number is:", m)
else:
    print("The largest number is:", p)