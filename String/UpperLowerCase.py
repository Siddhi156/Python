str = input("Enter string :")
upper = 0
lower = 0 

for i in str:
  if i.isupper():
    upper = upper +1
  else:
    lower = lower +1

print("No. of uppercase letters : ", upper)
print("No. of lowercase letters :", lower)
