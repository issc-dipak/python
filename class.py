# Define a class
class Student:
    # Constructor (initializer)
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

    # Method to check if student is adult
    def is_adult(self):
        return self.age >= 18


# Create objects (instances) of Student class
s1 = Student("Rahul", 20, 101)
s2 = Student("Anita", 16, 102)

# Access methods
s1.display()
print("Is adult:", s1.is_adult())

s2.display()
print("Is adult:", s2.is_adult())
