# 3: Remove an Item
tasks = ["study", "cook", "sleep", "cook"]
print(tasks)
tasks.remove("cook")
print(tasks)
if "walk" in tasks:
tasks.remove("walk")
else:
print("walk is not in the list")
tasks.remove("study")
print(tasks)