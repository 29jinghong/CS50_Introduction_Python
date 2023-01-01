cost = 50
money = [5, 25, 10]
while True:
    print("your total cost is:", cost)
    num = int(input("Enter here:"))
    for m in money:
        if m == num:
            cost = cost - num
            break
    if cost <= 0:
        print("Done")
        break