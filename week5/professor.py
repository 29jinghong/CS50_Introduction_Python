import random

def main():
    correct = 0
    wrong = 0
    twrong = 0
    total = 0

    while True:
        level = int(input("what is the level: "))
        #setting upper bound and lower bound
        upperBound = 10 ** level
        lowerBound = int(upperBound / 10)
        #generate random numbers based on uppwer bound and lower bound
        Num0, Num1 = generate_num(lowerBound, upperBound)
        if level != 0:
            break

    while True:
        print(Num0 , "+" , Num1 , "= ?")
        if total == 10:
            print("Corrcet:", correct,", Wrong:", twrong)
            break
        if wrong == 3:
            print(Num0, "+", Num1, "=", Num1 + Num0)
            twrong = twrong + 1
            Num0, Num1 = generate_num(lowerBound, upperBound)
            total = total + 1
            print("total:", total)
            wrong = 0
            continue
        try:
            NumI = int(input("answer: "))
        except:
            continue
        if NumI == Num1 + Num0:
            correct = correct + 1
            Num0, Num1 = generate_num(lowerBound, upperBound)
            print("correct:", correct)
            total = total + 1
            print("total:", total)
            continue
        else:
            wrong = wrong + 1
        
        

def generate_num(low, high):
    Num0 = random.randint(low, high)
    Num1 = random.randint(low, high)
    return Num0,Num1

main()
