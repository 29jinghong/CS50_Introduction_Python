import plates
    

def test_normal():
    result = True
    assert plates.is_valid("CS50") == result

    result = False
    assert plates.is_valid("CS05") == result

    result = True
    assert plates.is_valid("CS50P") == result

    result = True
    assert plates.is_valid("loser") == result

def test_with_symble():
    result = False
    assert plates.is_valid("PI3.14") == result

def test_one_letter():
    result = False
    assert plates.is_valid("Z") == result

    assert plates.is_valid("A") == result

def test_number():
    result = False
    assert plates.is_valid("0") == result

def test_one_symble():
    result = False
    assert plates.is_valid("!") == result
