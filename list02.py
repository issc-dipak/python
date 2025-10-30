
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("Length of list:", len(numbers))

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("\nAll elements:")
for num in numbers:
    print(num)

total = sum(numbers)
average = total / len(numbers)
print("\nSum:", total)
print("Average:", average)

numbers[2] = 99
print("\nUpdated List:", numbers)
