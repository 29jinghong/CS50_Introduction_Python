def main():
    word = input("Enter here: ")
    word = convert(word)
    print(word)

def convert(word):
    word = word.replace(":)", "🙂")
    word = word.replace(":(", "🙁")
    return word
main()