def main():
    list = {}

    while True:
        try:
            item = input.strip()
            list[item] = list.get(item, 0) + 1
        except EOFError:
            print()
            break

    for item in list:
        print(list[item], item.upper())

main()