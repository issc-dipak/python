
def left_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def right_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2*i - 1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2*i - 1))

def hollow_pyramid(n):
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - i) + "*")
        elif i == n:
            print("*" * (2*n - 1))
        else:
            print(" " * (n - i) + "*" + " " * (2*i - 3) + "*")

if __name__ == "__main__":
    n = int(input("Rows: "))
    print("\nLeft aligned:")
    left_triangle(n)
    print("\nRight aligned:")
    right_triangle(n)
    print("\nCentered pyramid:")
    pyramid(n)
    print("\nInverted pyramid:")
    inverted_pyramid(n)
    print("\nHollow pyramid:")
    hollow_pyramid(n)
