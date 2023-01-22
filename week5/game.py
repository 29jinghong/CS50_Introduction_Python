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
            right = random.randint(1, level)

        if num > right:
            print("too big")
        elif num < right:
            print("too small")
        else:
            print("Correct!")
            break

main()
