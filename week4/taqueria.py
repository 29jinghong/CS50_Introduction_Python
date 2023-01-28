def main():
    entrees: dict = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    total = 0.0

    while True:
        print("Menu:")
        print("Baja Taco : 4.00, Burrito : 7.50, Bowl : 8.50, Nachos : 11.00, Quesadilla : 8.50, Super Burrito : 8.50, Super Quesadilla : 9.50, Taco : 3.00, Tortilla Salad : 8.00,")
        print("'Type quit to quit'")
        try:
            item = input("Item: ").strip().title()
            if item == "Quit":
                break
        except EOFError:
            print()
            break

        total += entrees.get(item, 0)
        if item in entrees:
            print(f"Total ${total:.2f}\n")
        else:
            print("")

main()