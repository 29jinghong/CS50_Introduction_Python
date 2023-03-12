import twttr

def test_normal_words():
    result = twttr.check("number")
    assert result == "nmbr"

    result = twttr.check("assets")
    assert result == "ssts"
    

def test_int_numbers():
    result = twttr.check("0")
    assert result == "0"

    result = twttr.check("1234")
    assert result == "1234"
    
def test_non_value():
    result = twttr.check("")
    assert result == ""
    
def test_all_vovel():
    result = twttr.check("eeeeeeeuuuuuuiiiiiiooooaaaa")
    assert result == ""
