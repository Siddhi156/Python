# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('punkt_tab')

# text = "Python is easy to learn and very useful."

# words = word_tokenize(text)
# print("Word tokens:")
# print(words)

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Python is a high-level programming language and a powerful tool for data analysis, machine learning, and web development."

words = word_tokenize(text)
print("Word tokens:")
print(words)
