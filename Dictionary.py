

students = {}

while True:
    print("\n---- Student Dictionary Menu ----")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update marks")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} added successfully!")

    elif choice == '2':
        if not students:
            print("No students found.")
        else:
            for name, marks in students.items():
                print(f"{name}: {marks}")

    elif choice == '3':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == '4':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print(f"{name}'s marks updated!")
        else:
            print("Student not found.")

    elif choice == '5':
        name = input("Enter student name to delete: ")
        if students.pop(name, None) is not None:
            print(f"{name} deleted successfully.")
        else:
            print("Student not found.")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
