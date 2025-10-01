def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

nums = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original:", nums)
print("Without Duplicates:", remove_duplicates(nums))
