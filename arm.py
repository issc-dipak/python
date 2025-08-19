num = 153
power = len(str(num))
print("Armstrong" if num == sum(int(d)**power for d in str(num)) else "Not Armstrong")
