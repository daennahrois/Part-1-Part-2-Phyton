# 7: Sum of List Numbers
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
total += number
print("Total:", total)
print("Total using sum():", sum(numbers))
average = total / len(numbers)
print("Average:", average)