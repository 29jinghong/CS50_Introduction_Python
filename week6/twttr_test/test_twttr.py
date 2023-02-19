import twttr
def main():
    assert shorten("number", "numbr")
    assert shorten("assets", "assts")
    assert shorten("food", "fd")
    assert shorten("aeiouw", "aeiow")
    assert shorten("aa", "")
    assert shorten("eeeeeeeuuuuuuiiiiiiooooaaaa", "eeeeeeeuuuuuuiiiiiioooo")
    assert shorten("0a", "0")



def shorten(word, answer):
    checked = twttr.check(word)

    if checked == answer:
        print('"' + word + '"',"PASSED")
        return True
    else:
        print('"' + word + '"',"FAILED")
        return False
    

if __name__ == "__main__":
    main()
