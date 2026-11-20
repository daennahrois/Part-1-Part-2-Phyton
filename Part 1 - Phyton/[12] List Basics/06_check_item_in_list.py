# 6: Check if Item Exists in List
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
if "apple" in fruits:
print("Yes, apple is in the list")
if "mango" not in fruits:
print("No mango in the list")
search = "cherry"
if search in fruits:
print(search, "found at index", fruits.index(search))
else:
print(search, "not found")