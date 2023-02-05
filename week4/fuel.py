def main():
    while True:
        print("End program by Entering nothing")
        fuel = input("Fraction: ")
        try:
            num, div = fuel.split("/", 1)
            num = int(num)
            div = int(div)
            if num <= div:
                f = (round(num / div * 100))
        except ValueError or ZeroDivisionError:
            print("ValueError or ZeroDivisionEroor")
            pass
        try:
            if f == None:
                raise
                Exception
            if f <= 1:
                print("E")
                break
            elif f >= 99:
                print("F")
                break
            else:
                print(f"{f}%")
                break
        except Exception:
            print("Program ended")
            break
main()
