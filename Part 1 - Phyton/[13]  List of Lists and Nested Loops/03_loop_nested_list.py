# 3: Loop Through a Nested List
grid = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]
print(row)
print()
for row in grid:
for value in row:
print(value)
print()
for i in range(len(grid)):
for j in range(len(grid[i])):
print(f"grid[{i}][{j}] = {grid[i][j]}")