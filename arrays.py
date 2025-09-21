# Array problem solver in Python

def sum_of_array(arr):
    return sum(arr)

def find_min_max(arr):
    return min(arr), max(arr)

def reverse_array(arr):
    return arr[::-1]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # index
    return -1

def sort_array(arr):
    return sorted(arr)


# ---------------- Main Program -----------------
arr = []

n = int(input("Enter size of array: "))
print("Enter array elements:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

while True:
    print("\n--- Array Operations ---")
    print("1. Sum of array")
    print("2. Minimum & Maximum")
    print("3. Reverse array")
    print("4. Linear Search")
    print("5. Sort array")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sum of array:", sum_of_array(arr))

    elif choice == 2:
        mn, mx = find_min_max(arr)
        print("Minimum:", mn, "Maximum:", mx)

    elif choice == 3:
        print("Reversed array:", reverse_array(arr))

    elif choice == 4:
        target = int(input("Enter element to search: "))
        index = linear_search(arr, target)
        if index != -1:
            print(f"Element {target} found at index {index}")
        else:
            print("Element not found")

    elif choice == 5:
        print("Sorted array:", sort_array(arr))

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
