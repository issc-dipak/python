def fibonacci(n):
    """
    Generates the Fibonacci sequence up to a given number of terms.
    """
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
num_terms = 10
print(fibonacci(num_terms))

# Another example:
num_terms_2 = 5
print(fibonacci(num_terms_2))
