class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method banaya
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rahul", 20)

s1.show()
