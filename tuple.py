# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

print("Tuple:", my_tuple)

# Accessing elements (indexing starts from 0)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple can hold mixed data types
mixed_tuple = (1, "apple", 3.5, True)
print("Mixed Tuple:", mixed_tuple)

# Tuple unpacking
a, b, c = (100, 200, 300)
print("a =", a, "b =", b, "c =", c)

# Nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Element from nested tuple:", nested_tuple[1][1])

# Length of tuple
print("Length of my_tuple:", len(my_tuple))

# Check if element exists
print("Is 20 in my_tuple?", 20 in my_tuple)
print("Is 99 in my_tuple?", 99 in my_tuple)

# Tuple slicing
print("First three elements:", my_tuple[0:3])

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
print("Concatenated Tuple:", tuple1 + tuple2)

# Repetition
print("Repetition:", tuple1 * 3)
