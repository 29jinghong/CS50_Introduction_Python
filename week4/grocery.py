def main():
    print("type stop to stop.")
    list = {}

    while True:
        try:
            item = input().strip()
            if item.lower() == "stop":
                break
            list[item] = list.get(item, 0) + 1
        except EOFError:
            print("Done")
            break

    for item in list:
        print(list[item], item.upper())

main()