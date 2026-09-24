import re

text = "I have 2 books and 3 pens"
result = re.findall("[0-9]+", text)

print("Numbers found:", result)