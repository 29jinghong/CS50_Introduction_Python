def main():
    while True:
        print("End program by Entering nothing")
        fuel = input("Fraction: ")
        end = convert(fuel)
        if end == 1 or 2 or 3:
            break

def convert(fuel):
        try:
            num, div = fuel.split("/", 1)
            num = int(num)
            div = int(div)
            if num <= div:
                f = (round(num / div * 100))
        except ValueError or ZeroDivisionError:
            print("ValueError or ZeroDivisionEroor")
            return 3
        try:
            if f == None:
                raise
                Exception
            if f <= 1:
                print("E")
                return 1
            elif f >= 99:
                print("F")
                return 1
            else:
                print(f"{f}%")
                return 1
        except Exception:
            print("Program ended")
            return 2

main()
