# 8: Nested List Table
records = [
["Ana", 90, 85, 88],
["Ben", 75, 80, 78],
["Cara", 95, 92, 97]
]
print(f"{'Name':<8}{'Math':<8}{'Science':<8}{'English':<8}{'Average':<8}")
print("-" * 40)
for record in records:
name = record[0]
scores = record[1:]
average = sum(scores) / len(scores)
print(f"{name:<8}{scores[0]:<8}{scores[1]:<8}{scores[2]:<8}{average:
<8.2f}")
print()
best_average = 0
best_student = ""
for record in records:
average = sum(record[1:]) / len(record[1:])
if average > best_average:
best_average = average
best_student = record[0]
print(f"Top student: {best_student} ({best_average:.2f})")