def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    total = dollars + tip
    print(f"Leave ${total:.2f} in total.")


def dollars_to_float(d):
    d = float(d)
    return d


def percent_to_float(p):
    p = float(p)
    p = p/100
    return p

main()
