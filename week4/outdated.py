months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def main():
    print("Format: September 8, 1636 || 9/8/1636")
    while True:
        Rdate =  input("Date: ").strip()
        if "/" in Rdate:
            try:
                month, day, year = Rdate.split("/", 2)
                print(f"{year}-{month:02}-{day:02}")
                break
            except ValueError:
                print("there is a vlaue error, that occur")
                pass
            
        if  "," in Rdate:
            try:
                #September 8, 1636 
                date = Rdate.split(",")
                DM = date[0].split(" ")
                #just doing extra step to clear things
                if len(DM) == 2:
                    day, month, year = DM[1], months.index(DM[0]) + 1, date[1]
                    year = year.title()
                    print(f"{year}-{month:02}-{day:02}")
                else:
                    print("there is a vlaue error, that occur")
                break
            except ValueError:
                print("there is a vlaue error, that occur")
                pass
main()            
