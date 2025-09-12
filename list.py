# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])      # apple
print("Last fruit:", fruits[-1])      # cherry

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Inserting at a specific index
fruits.insert(1, "mango")
print("After insert:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Popping last element
last_item = fruits.pop()
print("Popped item:", last_item)
print("After pop:", fruits)

# Updating elements
fruits[0] = "grapes"
print("After update:", fruits)

# Looping through list
print("Looping through list:")
for f in fruits:
    print(f)

# List comprehension (squares of numbers 1–5)
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Checking membership
print("Is 'mango' in list?", "mango" in fruits)

# Length of list
print("Length:", len(fruits))
