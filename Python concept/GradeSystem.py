students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully!")

def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print("Grade updated successfully!")
    else:
        print("Student not found!")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully!")
    else:
        print("Student not found!")

def average_grade():
    if len(grades) == 0:
        print("No students in the list.")
    else:
        avg = sum(grades) / len(grades)
        print("Average Grade:", avg)

def highest_lowest():
    if len(grades) == 0:
        print("No students in the list.")
    else:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))

def display_students():
    if len(students) == 0:
        print("No students available.")
    else:
        print("\nStudent List:")
        for i in range(len(students)):
            print(students[i], "-", grades[i])

while True:
    print("\n----- Student Grade Management System -----")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Display Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Display Student List")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        average_grade()
    elif choice == "5":
        highest_lowest()
    elif choice == "6":
        display_students()
    elif choice == "7":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Please try again.")