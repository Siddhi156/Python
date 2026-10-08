import numpy as np
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
print("Enter elements for 1st array:")
arr1 = []
for i in range (r):
    row = []
    for j in range(c):
        x = int(input("Enter element:"))
        row.append(x)
    arr1.append(row)

print("Enter elements for 2nd array:")
arr2=[]
for i in range(r):
    row = []
    for j in range(c):
        x = int(input("Enter element:"))
        row.append(x)
    arr2.append(row)

a1 = np.array(arr1)
a2 = np.array(arr2)
print("\nThe 1st array is:")
print(a1)
print("\nThe 2nd array is :")
print(a2)

print("\nThe addition of 2 arrays is:")
print(a1+a2)

print("\nThe subtraction of 2 arrays is:")
print(a1-a2)

print("\nThe multiplication of 2 arrays is:")
print(a1*a2)

print("\nThe division of 2 arrays is:")
print(a1/a2)

print("\nThe transpose of 1st array is :")
print(a1.T)

print("\nThe transpose of 2nd array is:")
print(a2.T)





