def second_largest(arr):
    # Remove duplicates by converting to set
    unique_nums = list(set(arr))

    # If less than 2 unique elements, no second largest
    if len(unique_nums) < 2:
        return None

    # Sort in descending order
    unique_nums.sort(reverse=True)

    # Second largest will be at index 1
    return unique_nums[1]


# Example usage
arr = [12, 35, 1, 10, 34, 1, 35, 12]
print("Array:", arr)
print("Second largest:", second_largest(arr))
