# Swapping two numbers

# Input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
