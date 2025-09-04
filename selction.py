def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element is the minimum
        min_index = i
        # Find the minimum element in remaining array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


numbers = [64, 25, 12, 22, 11]
print("Original array:", numbers)
sorted_numbers = selection_sort(numbers)
print("Sorted array:", sorted_numbers)
