def main():
    print("End program by Entering control-c")
    while True:
        try:
            fuel = input("Fraction: ")
            if fuel == "":
                print("Entered nothing program Stoped")
                exit()
            num, div = fuel.split("/", 1)
            num = int(num)
            div = int(div)
            if num <= div:
                f = (round(num / div * 100))
        except ValueError or ZeroDivisionError:
            print("ValueError or ZeroDivisionEroor")
            exit()
        except KeyboardInterrupt:
            print()
            print("Program ended")
            exit()
        if num != None:
            break

    if f <= 1:
            print("E")
    elif f >= 99:
        print("F")
    else:
        print(f"{f}%")

main()
