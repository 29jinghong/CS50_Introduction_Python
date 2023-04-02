import re


def main():
    print(parse(input("HTML: ")))


def parse(link):
    matches = re.search(r"^<.*src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/(.+?)\".*>$", link)
    
    if matches:
        #group(1) Return the string matched by the RE
        return "https://youtu.be/" + matches.group(1)

    return None


if __name__ == "__main__":
    raise SystemExit(main())
