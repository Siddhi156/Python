arr = [9,12,34,5,46,1,89]
n = int(input("Enter a number to delete:"))
if n in arr:
    arr.remove(n)

print("Array after deletion:", arr)