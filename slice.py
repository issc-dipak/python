# Define a string
text = "BananaChips"

# Slice from index 0 to 5 (characters at 0,1,2,3,4)
print("Slice [0:6]:", text[0:6])   # Output: Banana

# Slice from index 6 to end
print("Slice [6:]:", text[6:])     # Output: Chips

# Slice from beginning to index 5 (excluding 5)
print("Slice [:5]:", text[:5])     # Output: Banan

# Slice the full string
print("Full string [::]:", text[::])  # Output: BananaChips

# Slice with step of 2
print("Every 2nd character [::2]:", text[::2])  # Output: Bnnahp

# Reverse the string using slicing
print("Reversed string [::-1]:", text[::-1])   # Output: spiCananaB
