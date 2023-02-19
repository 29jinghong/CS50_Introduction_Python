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
    print("Menu:")
    print("Baja Taco : 4.00, Burrito : 7.50, Bowl : 8.50, Nachos : 11.00, Quesadilla : 8.50, Super Burrito : 8.50, Super Quesadilla : 9.50, Taco : 3.00, Tortilla Salad : 8.00,")
    print("'Type control-c to quit'")
    while True:
        try:
            item = input("Item: ").strip().title()
        except KeyboardInterrupt:
            print()
            print("Done")
            break

        total += entrees.get(item, 0)
        if entrees.get(item, 0) != 0:
            print(f"added {item}")
        else:
            print(f"no such item as {item}")
    print(f"Total ${total:.2f}\n")

main()
