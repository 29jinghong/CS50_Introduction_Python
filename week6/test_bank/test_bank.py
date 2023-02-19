import bank

def main():
    assert value("How you doing?", "$20")
    assert value("What's happening?", "$100")
    assert value("What's up?", "$100")
    assert value("How's it going?", "$20")
    assert value("Hello ", "$0")
    assert value("Hello, Newman", "$0")
    assert value("How you doing", "$20")
    assert value("What's happening?", "$100")
    assert value("hello loser", "$100")
    assert value("no cap", "$100")
    assert value("jowrw4qrqwsafcxqrwefsdv", "$100")
    assert value("0", "$100")
    print("all test case passed")

def value(greeting, answer):
    checked = bank.check(greeting)
    print(checked, answer)
    if checked == answer:
        print('"' + greeting + '"', "PASSED")
        return True
    else:
        print('"' + greeting+ '"', "FAILED")
        return False

if __name__ == "__main__":
    main()