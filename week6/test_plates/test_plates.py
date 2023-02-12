import plates

def main():
    check_is_valid("CS50")
    check_is_valid("CS05")
    check_is_valid("CS50P")
    check_is_valid("PI3.14")
    check_is_valid("H")
    check_is_valid("OUTATIME")
    check_is_valid("0")
    check_is_valid("!")
    check_is_valid("qwer")
    check_is_valid("00000000000")
    check_is_valid("loser")
    check_is_valid("Jinghong29")

def check_is_valid(s):
    plate = plates.is_valid(s)

    answer = False
    
    length = len(s)
    if length > 1 and length < 7:
        for letters in s:
            if not s.isalnum():
                break

            if s[0:2].isalpha():
                middle = s[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break

                zeroIndex = s.find("0") - 1

                if s[-(zeroIndex)].isdigit():
                    for x in s:
                        if x.isdigit():
                            if x.startswith('0'):
                                answer = False
                            else:
                                answer = True

                if s[-2].isdigit() and s[-1].isalpha():
                    break
                elif s[-2].isdigit():
                    answer =  True
                elif s.isalpha():
                    answer = True

    else:
        answer = False

    if plate == answer:
        print('"' + s + '"',"PASSED")
    else:
        print('"' + s + '"',"FAILED")

if __name__ == "__main__":
    main()