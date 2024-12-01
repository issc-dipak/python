# Table 1: Multiplication Table for 2
table1 = [[f"{2} x {i} = {2*i}" for i in range(1, 6)]]

# Table 2: Multiplication Table for 3
table2 = [[f"{3} x {i} = {3*i}" for i in range(1, 6)]]

# Printing Tables Side by Side
print("Table for 2".ljust(20) + "Table for 3")
print("=" * 40)

for row1, row2 in zip(table1[0], table2[0]):
    print(row1.ljust(20) + row2)
