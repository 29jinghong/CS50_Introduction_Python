num = 3
if num == 3:
    x = 3

print(x)

list = {"i":5,"o":7}
for i in list:
    print(i)

import random

level = 3

upperBound = 10 ** level
lowerBound = int(upperBound / 10)
num = random.randint(lowerBound, upperBound)

def generate_num(low, high):
    Num0 = random.randint(low, high)
    Num1 = random.randint(low, high)
    return Num0,Num1

Num0, Num1 = generate_num(lowerBound, upperBound)
print(Num0,Num1)