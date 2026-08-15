students = []


# 1. Add Student
def add_student():

    print("\n===== ADD STUDENT =====")

    name = input("Enter name: ")
    roll_no = int(input("Enter roll no: "))
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    print("\nEnter Marks")

    python_marks = float(input("Enter Python marks: "))
    english_marks = float(input("Enter English marks: "))
    maths_marks = float(input("Enter Maths marks: "))

    total = python_marks + english_marks + maths_marks
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"

    student = [
        name,
        roll_no,
        age,
        course,
        python_marks,
        english_marks,
        maths_marks,
        total,
        percentage,
        grade
    ]

    students.append(student)

    print("\nStudent added successfully!")


# 2. Display All Students
def display_all_students():

    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No students found.")

    else:
        for student in students:

            print("\nName:", student[0])
            print("Roll No:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Python Marks:", student[4])
            print("English Marks:", student[5])
            print("Maths Marks:", student[6])
            print("Total:", student[7])
            print("Percentage:", student[8])
            print("Grade:", student[9])

            print("------------------------")


# 3. Display Student by Roll No
def search_student():

    print("\n===== SEARCH STUDENT =====")

    search_roll = int(input("Enter roll no: "))

    found = False

    for student in students:

        if student[1] == search_roll:

            print("\n===== STUDENT DETAILS =====")

            print("Name:", student[0])
            print("Roll No:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Python Marks:", student[4])
            print("English Marks:", student[5])
            print("Maths Marks:", student[6])
            print("Total:", student[7])
            print("Percentage:", student[8])
            print("Grade:", student[9])

            found = True
            break

    if found == False:
        print("Student not found.")


# 4. Update Student
def update_student():

    print("\n===== UPDATE STUDENT =====")

    update_roll = int(input("Enter roll no to update: "))

    found = False

    for student in students:

        if student[1] == update_roll:

            print("\nStudent Found!")

            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_course = input("Enter new course: ")

            print("\nEnter New Marks")

            new_python = float(input("Enter Python marks: "))
            new_english = float(input("Enter English marks: "))
            new_maths = float(input("Enter Maths marks: "))

            total = new_python + new_english + new_maths
            percentage = total / 3

            if percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            elif percentage >= 35:
                grade = "D"
            else:
                grade = "Fail"

            student[0] = new_name
            student[2] = new_age
            student[3] = new_course
            student[4] = new_python
            student[5] = new_english
            student[6] = new_maths
            student[7] = total
            student[8] = percentage
            student[9] = grade

            found = True

            print("\nStudent updated successfully!")

            break

    if found == False:
        print("Student not found.")


# 5. Delete Student
def delete_student():

    print("\n===== DELETE STUDENT =====")

    delete_roll = int(input("Enter roll no to delete: "))

    found = False

    for student in students:

        if student[1] == delete_roll:

            students.remove(student)

            found = True

            print("Student deleted successfully!")

            break

    if found == False:
        print("Student not found.")


# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Display Student by Roll No")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_all_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 6.")
