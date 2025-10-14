for num in range(100, 1000):
    power = len(str(num))
    if num == sum(int(d)**power for d in str(num)):
        print(num, end=" ")
