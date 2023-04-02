import re

def main():
    print(count(input("Text: ")))

def count(text):
    #finds all the um with ignorecase.
    matches = re.findall(r"\bum\b", text, flags=(re.IGNORECASE))

    if matches:
        return len(matches)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    