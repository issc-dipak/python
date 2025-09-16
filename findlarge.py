def find_max(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

numbers = [12, 45, 7, 89, 23, 67]
print("List:", numbers)
print("Largest element:", find_max(numbers))
