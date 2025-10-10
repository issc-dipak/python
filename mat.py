import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = np.random.randint(1, 10, (rows, cols))
B = np.random.randint(1, 10, (cols, rows))

C = np.dot(A, B)

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix Multiplication Result (A × B):\n", C)
