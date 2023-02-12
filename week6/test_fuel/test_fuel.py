import fuel

def main():
    convert("0/4", 1)
    convert("3/4", 1)
    convert("1/4", 1)
    convert("4/4", 1)
    convert("23/54", 1)
    convert("33/4", 2)
    convert("1/0", 2)
    convert("0", 3)

def convert(fuels, answer):
    fraction = fuel.convert(fuels)
    if answer == fraction:
        print('"' + fuels + '"' , "PASSED")
    else:
        print('"' + fuels + '"' , "FAILED")

if __name__ == "__main__":
    main()