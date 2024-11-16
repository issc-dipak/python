num = 29
is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(f"{num} is Prime" if is_prime else f"{num} is not Prime")
