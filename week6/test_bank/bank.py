def main():
    greeting = input("Greeting: ").strip().upper()
    output = check(greeting)
    print(output)

def check(greeting):
    if greeting.startswith("H"):
        if greeting.startswith("HELLO"):
            return "$0"
        else:
            return"$20"
    else:
        return "$100"

main()
