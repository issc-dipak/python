
nums = [10, 20, 30, 40, 50, 60, 70]

s1 = slice(1, 5)      # index 1 se 4 tak
s2 = slice(0, 7, 2)   # 0 se 6 tak, step = 2

print("Original List:", nums)

print("slice(1,5):", nums[s1])    # [20, 30, 40, 50]
print("slice(0,7,2):", nums[s2])  # [10, 30, 50, 70]

text = "PythonProgramming"
s3 = slice(0, 6)   # first 6 characters
print("slice on string:", text[s3])  # Python
