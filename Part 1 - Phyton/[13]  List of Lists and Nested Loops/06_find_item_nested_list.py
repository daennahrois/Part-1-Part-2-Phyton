# 6: Find an Item in a Nested List
grid = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]
target = 50
found = False
for i in range(len(grid)):
for j in range(len(grid[i])):
if grid[i][j] == target:
print(f"{target} found at row {i}, column {j}")
found = True
break
if found:
break
if not found:
print(target, "not found")
print()
students = [
["Ana", 90],
["Ben", 85],
["Cara", 92]
]
search = "Ben"
for student in students:
if student[0] == search:
print(search, "has a score of", student[1])