import plates

def main():
    assert check_is_valid("CS50", True)
    assert check_is_valid("CS05", False)
    assert check_is_valid("CS50P", True)
    assert check_is_valid("PI3.14", False)
    assert check_is_valid("H", False)
    assert check_is_valid("OUTATIME", False)
    assert check_is_valid("0", False)
    assert check_is_valid("!", False)
    assert check_is_valid("qwer", True)
    assert check_is_valid("00000000000", False)
    assert check_is_valid("loser", True)
    assert check_is_valid("Jinghong29", False)
    print("all test case passed")

def check_is_valid(word, answer):
    plate = plates.is_valid(word)
    
    if plate == answer:
        print('"' + word + '"',"PASSED")
        return True
    else:
        print('"' + word + '"',"FAILED")
        return False
    

if __name__ == "__main__":
    main()
