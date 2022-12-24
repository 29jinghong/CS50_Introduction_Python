question = input("Expression: ")
num1, equation, num2 = question.strip().split()

num1 = float(num1)
num2 = float(num2)

if equation == "*":
    print(num1 * num2)
elif equation == "/":
    print(num1/num2) 
elif equation == "-":
    print(num1 - num2)
else:
    print(num1 + num2)