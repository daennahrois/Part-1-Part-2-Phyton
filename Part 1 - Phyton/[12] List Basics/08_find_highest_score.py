# 8: Find the Highest Score
scores = [78, 92, 85, 67, 99, 88]
highest = scores[0]
for score in scores:
if score > highest:
highest = score
print("Highest score:", highest)
print("Highest using max():", max(scores))
lowest = scores[0]
for score in scores:
if score < lowest:
lowest = score
print("Lowest score:", lowest)
names = ["Ana", "Ben", "Carla", "Dan", "Ella", "Fred"]
top_index = scores.index(highest)
print("Top student:", names[top_index])