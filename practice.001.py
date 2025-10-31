def rotate_right(a, k):
    n = len(a)
    if n == 0: return
    k %= n
    a[:] = a[::-1]
    a[:k] = a[:k][::-1]
    a[k:] = a[k:][::-1]

arr = [1,2,3,4,5,6,7]
rotate_right(arr, 3)
print(arr)  # [5,6,7,1,2,3,4]
