import fuel

def main():
    assert convert("0/4", "E")
    assert convert("3/4", "75%")
    assert convert("1/4", "25%")
    assert convert("4/4", "F")
    assert convert("23/54", "43%")
    assert convert("33/4", "divider less than divided, expected:(3/4)")
    assert convert("1/0", "divider less than divided, expected:(3/4)")
    assert convert("0", "ValueError or ZeroDivisionEroor")
    print("all test case passed")

def convert(fuels, answer):
    fraction = fuel.convert(fuels)
    if answer == fraction:
        print('"' + fuels + '"' , "PASSED")
        return True
    else:
        print('"' + fuels + '"' , "FAILED")
        return False

if __name__ == "__main__":
    main()