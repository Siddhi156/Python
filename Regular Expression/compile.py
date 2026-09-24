import re
pattern = re.compile("Python")
text = "I am learning Python"
result = pattern.search(text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")