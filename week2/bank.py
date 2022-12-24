answer = input("Greeting: ").strip().upper()

if answer.startswith("H"):
    if answer.startswith("HELLO"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")