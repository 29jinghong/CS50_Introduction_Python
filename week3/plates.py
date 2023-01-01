def main():
    plate = input("Enter here: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    length = len(plate)
    if length > 1 and length < 7:
        for letters in plate:
            if not plate.isalnum():
                break

            if plate[0:2].isalpha():
                middle = plate[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break

                zeroIndex = plate.find("0") - 1

                if plate[-(zeroIndex)].isdigit():
                    for x in plate:
                        if x.isdigit():
                            if x.startswith('0'):
                                return False
                            else:
                                return True

                if plate[-2].isdigit() and plate[-1].isalpha():
                    break
                elif plate[-2].isdigit():
                    return True
                elif plate.isalpha():
                    return True

    else:
        return False

main()
