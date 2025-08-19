
subject = input("Enter subject name: ")

marks = int(input(f"Enter marks in {subject}: "))

print(f"Marks in {subject} = {marks}")

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade in {subject}: {grade}")
