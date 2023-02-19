import twttr
def main():
    assert shorten("number", "nmbr")
    assert shorten("assets", "ssts")
    assert shorten("food", "fd")
    assert shorten("aeiouw", "w")
    assert shorten("aa", "")
    assert shorten("eeeeeeeuuuuuuiiiiiiooooaaaa", "")
    assert shorten("0a", "0")
    print("all test case passed")




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
