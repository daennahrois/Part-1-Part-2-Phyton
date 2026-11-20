# 7: Flatten Nested List
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Using nested for loops
flat = []
for row in nested:
for number in row:
flat.append(number)
print(flat)
# Using a list comprehension
flat = [number for row in nested for number in row]
print(flat)