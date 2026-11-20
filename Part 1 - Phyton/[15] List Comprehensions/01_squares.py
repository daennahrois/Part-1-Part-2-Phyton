# 1: Squares
squares = []
for x in range(1, 6):
squares.append(x ** 2)
print(squares)
squares = [x ** 2 for x in range(1, 6)]
print(squares)