n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
p = int(input("Enter third number: "))
if n < m and n < p:
    print("The smallest number is:", n) 
elif m < n and m < p:
    print("The smallest number is:", m)
else:
    print("The smallest number is:", p)