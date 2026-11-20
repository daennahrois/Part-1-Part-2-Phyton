# 4: Display a Matrix
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
for row in matrix:
for value in row:
print(value, end=" ")
print()
print()
for row in matrix:
for value in row:
print(value, end="\t")
print()
print()
for row in matrix:
print(" ".join(str(value) for value in row))