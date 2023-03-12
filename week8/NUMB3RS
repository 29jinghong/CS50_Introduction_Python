import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #searches for 1 or more any character, serch for a dot.
    #repeat that 4 times
    matches = re.search(r".+\..+\..+\..+", ip)

    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    raise SystemExit(main())
