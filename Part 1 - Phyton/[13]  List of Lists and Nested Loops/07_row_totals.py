# 7: Row Totals and Column Totals
sales = [
[120, 150, 100],
[200, 180, 220],
[90, 110, 130]
]
for i in range(len(sales)):
row_total = 0
for value in sales[i]:
row_total += value
print(f"Row {i + 1} total: {row_total}")
print()
for col in range(len(sales[0])):
col_total = 0
for row in sales:
col_total += row[col]
print(f"Column {col + 1} total: {col_total}")
print()
highest_row = 0
highest_total = sum(sales[0])
for i in range(1, len(sales)):
if sum(sales[i]) > highest_total:
highest_total = sum(sales[i])
highest_row = i
print(f"Highest row: Row {highest_row + 1} with {highest_total}")