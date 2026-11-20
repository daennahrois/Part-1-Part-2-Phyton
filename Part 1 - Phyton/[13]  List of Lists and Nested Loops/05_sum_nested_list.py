# 5: Sum of All Numbers in a Nested List
numbers = [
[5, 10, 15],
[20, 25, 30],
[35, 40, 45]
]
total = 0
for row in numbers:
for value in row:
total += value
print("Total:", total)
total = 0
for row in numbers:
total += sum(row)
print("Total using sum():", total)
count = 0
for row in numbers:
count += len(row)
print("Number of items:", count)
print("Average:", total / count)