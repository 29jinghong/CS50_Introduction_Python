
import sys


def main():
    argc = len(sys.argv)

    if argc < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif argc > 2:
        print("Too many command-line arguments")
        sys.exit(2)

    if (not sys.argv[1].endswith(".py")):
        print("Not a python file")
        sys.exit(3)

    try:
        with open(sys.argv[1]) as file:
            code = 0

            for line in file:
                if is_code(line):
                    code += 1

            print(code)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(4)

    return 0


def is_code(line):
    if line.lstrip().startswith("#") or line.lstrip() == "":
        return False
    return True


if __name__ == "__main__":
    raise SystemExit(main())