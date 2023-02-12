def main():
    words = input("Enter here:")
    c_word = check(words)
    print(c_word)

def check(words):
    aferbet = ["a", "e", "i", "o", "u"]
    for word in words:
        if word.lower() in aferbet:
            a_word = words.replace(word.lower(), "")
    pword = words
    return a_word , pword

