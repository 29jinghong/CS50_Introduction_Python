aferbet = ["a", "e", "i", "o", "u"]

words = input("Enter here:")
for word in words:
    if word.lower() in aferbet:
        words = words.replace(word.lower(), "")

print(words)