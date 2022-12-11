def main():
    number = int(input("m = : "))
    number = exchange(number)
    print("E = : ",number)

def exchange(num):
    num = num * 90000000000000000
    return num

main()
