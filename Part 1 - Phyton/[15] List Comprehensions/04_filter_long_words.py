# 4: Filter Long Words
words = ["cat", "elephant", "dog", "giraffe", "fish", "tiger"]
long_words = [word for word in words if len(word) > 5]
print(long_words)