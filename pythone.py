def max_subarray_sum(arr):
    max_so_far = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        # Either extend the current subarray or start a new one
        current_sum = max(arr[i], current_sum + arr[i])
        max_so_far = max(max_so_far, current_sum)

    return max_so_far


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Array:", arr)
print("Maximum Subarray Sum:", max_subarray_sum(arr))
