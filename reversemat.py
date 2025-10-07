def reverse_alternating_matrix(n):
    num = 1
    matrix = []

    for i in range(1, n + 1):
        # Row ke numbers range se banao
        row = list(range(num, num + n))
        num += n

        # Even row ho to reverse kar do
        if i % 2 == 0:
            row.reverse()

        matrix.append(row)

    # Print nicely
    for row in matrix:
        print(' '.join(str(x).rjust(3) for x in row))

# Example
n = int(input("Enter n: "))
reverse_alternating_matrix(n)
