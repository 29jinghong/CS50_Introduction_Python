def main():
    while True:
        print("End program by Entering nothing")
        fuel = input("Fraction: ")
        end = convert(fuel)
        print(end)

def convert(fuel):
        try:
            num, div = fuel.split("/", 1)
            num = int(num)
            div = int(div)
            if num <= div:
                f = (round(num / div * 100))
        except ValueError or ZeroDivisionError:
            return "ValueError or ZeroDivisionEroor"
        try:
            if f == None:
                raise
                Exception
            if f <= 1:
                return "E"
            elif f >= 99:
                return "F"
            else:
                return str(f) + "%"
        except Exception:
            print("Program ended")
            return "divider less than divided, expected:(3/4)"

if __name__ == "__main__":
    main()
    