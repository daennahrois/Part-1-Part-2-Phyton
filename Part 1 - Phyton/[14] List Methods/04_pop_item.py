# 4: Pop an Item
letters = ["a", "b", "c", "d", "e"]
print(letters)
last = letters.pop()
print("Removed:", last)
print(letters)
second = letters.pop(1)
print("Removed:", second)
print(letters)
while len(letters) > 0:
print("Popping:", letters.pop())
print(letters)