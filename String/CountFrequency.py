str = input("Enter a string : ")
ch = input("Enter the character to count its frequency :")
count = 0
for i in str :
   if i == ch:
      count = count +1
print("Frequency count is : ",count)