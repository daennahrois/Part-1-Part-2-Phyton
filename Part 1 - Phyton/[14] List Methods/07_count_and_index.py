# 7: Count and Index
votes = ["yes", "no", "yes", "yes", "no"]
print("Yes votes:", votes.count("yes"))
print("No votes:", votes.count("no"))
print("Maybe votes:", votes.count("maybe"))
print("First yes at index:", votes.index("yes"))
print("First no at index:", votes.index("no"))
word = "maybe"
if word in votes:
print(word, "is at index", votes.index(word))
else:
print(word, "is not in the list")