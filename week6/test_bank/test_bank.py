import bank

def main():
    value("How you doing?")
    value("What's happening?")
    value("What's up?")
    value("How's it going?")
    value("Hello")
    value("Hello, Newman")
    value("How you doing")
    value("What's happening?")
    value("hello loser")
    value("no cap")
    value("jowrwqrqwsafcxqrwefsdv")
    value("0")

def value(greeting):
    checked = bank.check(greeting)
    if greeting.startswith("H"):
        if greeting.startswith("HELLO"):
            answer = "$0"
        else:
            answer = "$20"
    else:
        answer = "$100"
    if answer == checked:
        return print('"' + greeting + '"', "PASSED")
    else:
        return print('"' + greeting+ '"', "FAILED")

if __name__ == "__main__":
    main()