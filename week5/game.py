import random

def main():
    level = 0
    num = 0
    right = 0
    while True:
        try:
            if level == 0:
                level = int(input("What Level: "))
            num = int(input("guess: "))
        except:
            continue
        if right == 0:
            upperBound = 10 ** level
            lowerBound = int(upperBound / 10)
            right = random.randint(lowerBound, upperBound)

        if num > right:
            print("too big")
        elif num < right:
            print("too small")
        else:
            print("Correct!")
            break

main()
