start = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0
for num in range(start, end + 1):
    digit_sum = sum(int(d) for d in str(num))
    if digit_sum != 0 and num % digit_sum == 0:
        count += 1

print("Numbers divisible by the sum of their digits:", count)
