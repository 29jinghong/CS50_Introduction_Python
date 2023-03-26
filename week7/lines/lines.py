import sys

def main():
    validate_input_args()
    lines = counting_input_lines()
    print(lines)

def is_code(line : str):
    if line.lstrip().startswith("#") or line.lstrip() == "":
        return False
    return True

def counting_input_lines():
    try:
        with open(sys.argv[1]) as file:
            num = 0

            for line in file:
                if is_code(line):
                    num += 1

            return num

    except FileNotFoundError:
        sys.exit("File does not exist")

def validate_input_args():
    arg_lengt = len(sys.argv)
    if arg_lengt < 2:
       sys.exit("Too few command-line arguments")
    elif arg_lengt > 2:
       sys.exit("Too many command-line arguments")

    if (not sys.argv[1].endswith(".py")):
       sys.exit("Not a python file")

    return arg_lengt

#^can use mock to test the above code.

if __name__ == "__main__":
    raise SystemExit(main())

# this ^ runs the main function then exit 
#so SystemExit runs the function insdie the () and then exit the program. 
#test line 15(finding file) next test line 24(check on how to test for exception).
