import re
text = "I am learning Python"
result = re.search("Python", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")