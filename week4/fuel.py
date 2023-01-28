def main():
    fuel = input("Fraction: ")
    try:
        num, div = fuel.split("/", 1)
        num = int(num)
        div = int(div)
        if num <= div:
            f = (round(num / div * 100))
    except ValueError or ZeroDivisionError:
        pass
    try:
        if f <= 1:
            print("E")
        elif f >= 99:
            print("F")
        else:
            print(f"{f}%")
    except UnboundLocalError:
        pass
main()
