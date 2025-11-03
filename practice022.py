

students = (
    ("Dipak", (85, 90, 88)),
    ("Riya", (78, 85, 80)),
    ("Amit", (92, 88, 95)),
    ("Sneha", (70, 75, 72)),
    ("Karan", (88, 92, 90))
)

def average(marks):
    return sum(marks) / len(marks)

averages = tuple((name, average(marks)) for name, marks in students)

sorted_students = tuple(sorted(averages, key=lambda x: x[1], reverse=True))

topper = sorted_students[0]

print("=== Student Average Marks ===")
for name, avg in sorted_students:
    print(f"{name:10} → {avg:.2f}")

print("\n🏆 Topper:", topper[0])
print("🎯 Highest Average Marks:", topper[1])

names, marks = zip(*students)
print("\nAll Student Names:", names)
print("All Marks Tuples:", marks)

all_marks = tuple(mark for sub in marks for mark in sub)
print("\nAll Marks Combined:", all_marks)
print("Overall Average:", sum(all_marks)/len(all_marks))
