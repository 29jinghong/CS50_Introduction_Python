def main():
    words = input("Enter here:")
    c_word = check(words)
    print(c_word)

def check(words):
    aferbet = ["a", "e", "i", "o", "u"]
    for word in words:
        if word.lower() in aferbet:
            words = words.replace(word.lower(), "")
    return words

if __name__ == "__main__":
    main()
    