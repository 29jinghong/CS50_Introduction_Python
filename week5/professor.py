import random

def main():
    Num0 = 0
    Num1 = 0
    level = 0
    wrong = 0

    while True:
        if level == 0:
            try:
                level = int(input("what is the level: "))
                Num0 = random.randint(1, level)
                Num1 = random.randint(1, level)
            except:
                continue
        
        if level != 0:
            print(Num0 , "+" , Num1 , "= ?")
            try:
                NumI = int(input("answer: "))
            except:
                continue
            if NumI == Num1 + Num0:
                print("correct")
                break
            else:
                wrong = wrong + 1
    
            if wrong == 4:
                print(Num0, "+", Num1, "=", Num1 + Num0)
                break

        
main()
