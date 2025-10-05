arr = [1, 2, 2, 3, 1, 4, 2, 5]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of elements:")
for key, value in freq.items():
    print(f"{key}: {value}")
