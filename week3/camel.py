

def main():
    text = input("Enter here: ")
    print(camelToSnake(text))


def camelToSnake(text):
   for l in text:
        if l.isupper():
            text = text.replace(l, "_" + l.lower())
            return text


main()
