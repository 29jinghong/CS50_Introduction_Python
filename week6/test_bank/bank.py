def main():
    greeting = input("Greeting: ").strip().lower()
    output = check(greeting)
    print(output)

def check(greeting):
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return "$0"
        else:
            return"$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
    