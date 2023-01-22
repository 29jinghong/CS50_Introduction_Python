def main():
    fuel = ("Fraction: ")
    try:
        num, div = fuel.split("/", 1)
        if num <= div:
            f = (round(num / div * 100))
    except ValueError or ZeroDivisionError:
        pass
    if f <= 1:
        print("E")
    elif f >= 99:
        print("F")
    else:
        print(f"{f}%")

main()