str = input("Enter a string: ")
count = 0
for i in str:
    if i in "aeiouAEIOU":
        count = count +1
print("Number of vowels in the string is :",count)

c = 0
space = 0
digit = 0
special_character = 0
for i in str:
    if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        c = c+1
    elif i == " ":
        space = space +1
    elif "0"<= i <="9":
        digit = digit +1
    else:
        special_character+=1
print("Number of consonants in the string is :",c)
print("Number of spaces in the string is :",space)
print("Number of digits in the string is :",digit)
print("Number of special characters in the string is :",special_character)


