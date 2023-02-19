def main():
    print("type control-c to stop.")
    list = {}

    while True:
        try:
            item = input().strip()
            list[item] = list.get(item, 0) + 1
        except KeyboardInterrupt:
            print()
            print("Done")
            break

    for item in list:
        print(list[item], item.upper())

main()
