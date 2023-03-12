import fuel

def test_empty():
    result = "E"
    assert fuel.convert("0/4") == result

    assert fuel.convert("0/15") == result

def test_full():
    result = "F"
    assert fuel.convert("4/4") == result

    assert fuel.convert("10/10") == result

def test_normal():
    result = "75%"
    assert fuel.convert("3/4") == result

    result = "43%"
    assert fuel.convert("23/54") == result

def test_invalid_divider_less_than_divided():
    result = "divider less than divided, expected:(3/4)"
    assert fuel.convert("33/4") == result

    assert fuel.convert("3/1") == result

    assert fuel.convert("13/0") == result

def test_invalid_zero_divider():
    result = "ValueError or ZeroDivisionEroor"
    assert fuel.convert("0") == result

    
