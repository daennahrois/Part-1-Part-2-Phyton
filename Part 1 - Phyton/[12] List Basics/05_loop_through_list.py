# 5: Loop Through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)
print()
for i in range(len(fruits)):
print(i, fruits[i])
print()
for index, fruit in enumerate(fruits):
print(index, fruit)
print()
i = 0
while i < len(fruits):
print(fruits[i])
i += 1