import plates
    

def test_normal():
    assert plates.is_valid("CS50") == True

    assert plates.is_valid("CS05") == False

    assert plates.is_valid("CS50P") == True

    assert plates.is_valid("loser") == True

def test_with_symble():
    assert plates.is_valid("PI3.14") == False

def test_one_letter():
    assert plates.is_valid("Z") == False

    assert plates.is_valid("A") == False

def test_number():
    assert plates.is_valid("0") == False

def test_one_symble():
    assert plates.is_valid("!") == False
