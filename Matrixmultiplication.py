import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix multiplication
C = np.dot(A, B)

# Print results
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix Multiplication (A × B):\n", C)
