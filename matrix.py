# Matrix using lists
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

# Matrix addition
result_add = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Matrix subtraction
result_sub = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Matrix multiplication (dot product)
result_mul = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
               for j in range(len(B[0]))] for i in range(len(A))]

print("Matrix A:", A)
print("Matrix B:", B)
print("A + B =", result_add)
print("A - B =", result_sub)
print("A × B =", result_mul)
