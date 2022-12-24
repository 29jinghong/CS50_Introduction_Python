hr, min = input("What time is it? : ").strip().split(":")

hr = float(hr)
min = float(min)

time = hr + (min/60)

if time > 7 and time <= 8:
    print("breakfast time")

if time > 12 and time <= 13:
    print("lunch time")

if time > 18 and time <= 19:
    print("dinner time")