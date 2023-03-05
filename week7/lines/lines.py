import sys


def main():
    argc = len(sys.argv)

    if argc < 2:
        sys.exit("Too few command-line arguments")
    elif argc > 2:
        sys.exit("Too many command-line arguments")

    if (not sys.argv[1].endswith(".py")):
        sys.exit("Not a python file")

    try:
        with open(sys.argv[1]) as file:
            code = 0

            for line in file:
                if is_code(line):
                    code += 1

            print(code)

    except FileNotFoundError:
        sys.exit("File does not exist")

    return 0


def is_code(line):
    if line.lstrip().startswith("#") or line.lstrip() == "":
        return False
    return True


if __name__ == "__main__":
    raise SystemExit(main())
# this ^ runs the main function then exit 
#so SystemExit runs the function insdie the () and then exit the program. 

#def check_argc():
#   argc = len(sys.argv)
#   if argc < 2:
#        sys.exit("Too few command-line arguments")
#    elif argc > 2:
#        sys.exit("Too many command-line arguments")
#
#    if (not sys.argv[1].endswith(".py")):
#        sys.exit("Not a python file")
#   
#   return argc
#is this ^ better or worse and how do you test this kind of function if its used.
