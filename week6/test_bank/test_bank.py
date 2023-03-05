import bank

def test_20_dollor():
    result = "$20"
    assert bank.check("How you doing?") == result

    result = "$20"
    assert bank.check("How's it going?") == result

    result = "$20"
    assert bank.check("Hi how are you?") == result

def test_0_dollor():
    result = "$0"
    assert bank.check("hello") == result

    result = "$0"
    assert bank.check("hello, Newman") == result

def test_100_dollor():
    result = "$100"
    assert bank.check("0") == result

    result = "$100"
    assert bank.check("whats up") == result

    result = "$100"
    assert bank.check("qwerqwer") == result

