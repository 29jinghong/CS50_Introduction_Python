import twttr
def main():
    

    assert shorten("assets", "ssts")
    assert shorten("food", "fd")
    assert shorten("aeiouw", "w")
    assert shorten("", "")
    assert shorten("eeeeeeeuuuuuuiiiiiiooooaaaa", "")
    assert shorten("0", "0")


def shorten(word, answer):
    checked = twttr.check(word)

    return checked == answer

def test_normal_words():
    result = twttr.check("number")
    assert result == "nmbr"

def test_2():
    result = twttr.check("assets")
    assert result == "ssts"

def test_3():
    result = twttr.check("number")
    assert result == "nmbr"

if __name__ == "__main__":
    main()
    
