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
    while True:
        Rdate =  input("Date: ").strip()
        if "/" in Rdate:
            try:
                month, day, year = Rdate.split("/", 2)
                print(f"{year}-{month:02}-{day:02}")
                break
            except ValueError:
                pass
            
        if  "," in Rdate:
            try:
                #September 8, 1636 
                date = Rdate.split(",")
                DM = date[0].split(" ")
                #just doing extra step to clear things
                day, month, year = DM[1], months.index(DM[0]) + 1, date[1]
                print(f"{year}-{month:02}-{day:02}")
                break
            except ValueError:
                pass

            
