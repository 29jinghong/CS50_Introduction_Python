import twttr
def main():
    shorten("number")
    shorten("assets")
    shorten("food")
    shorten("aeiouw")
    shorten("aa")
    shorten("eeeeeeeuuuuuuiiiiiiooooaaaa")
    shorten("0a")



def shorten(word):
    checked = twttr.check(word)
    print("checking:", word)
    list = ["a", "e", "i", "o", "u"]
    for letter in list:
        if letter in checked:
            print("letter", letter, "failed")
        else:
            print("letter", letter, "pass")

if __name__ == "__main__":
    main()
