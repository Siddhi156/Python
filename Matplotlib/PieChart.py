import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'C++', 'SQL']
marks = [35, 20, 25, 16]
plt.pie(marks, labels = subjects, autopct = "%1.1f%%")
plt.title("Subject Marks Distribution")
plt.show()