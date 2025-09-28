# Numbers from 1 to 100 divisible by 5
total = 0

print("Numbers divisible by 5 between 1 and 100:")

for i in range(1, 101):   # 1 se 100 tak loop
    if i % 5 == 0:        # check divisibility
        print(i, end=" ")
        total += i        # sum add karo

print("\n\nSum of these numbers:", total)
