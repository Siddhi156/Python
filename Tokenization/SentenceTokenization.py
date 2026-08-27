# import nltk
# from nltk.tokenize import sent_tokenize

# nltk.download('punkt')
# text = "Python is a high-level programming language. It is very powerful and widely used."

# sentences = sent_tokenize(text)
# print("Sentence tokens:")
# print(sentences)

import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
text = "Python is a high-level programming language.It is very powerful and widely used.It is great for data analysis, machine learning, and web development."

sentences = sent_tokenize(text)
print("Sentence tokens:")
print(sentences)
