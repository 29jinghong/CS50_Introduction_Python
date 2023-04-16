import sys
import re
from datetime import date
from inflect import engine

def main():
# get birthday
    birthday_str = input("Date of Birth: ").strip()

    if not validate(birthday_str):
        sys.exit("Invalid date")
    #uses map to do the job it will return a map function which can be saved as a list
    year, month, day = map(int, birthday_str.split("-"))
    
    #this create a date object useing datetime
    birthday = date(year, month, day)

    # get today uesing datetime
    today = date.today()

    # get minutes(int) elapsed since birth
    minutes_int = (today - birthday).days * 24 * 60

    # convert minutes(int) to words useing inflect
    p = engine()
    minutes_str = p.number_to_words(minutes_int)
    minutes_str = minutes_str.replace('and ', '').capitalize()
    print(minutes_str, "minutes")

    return 0

def validate(birthday):
    #check if birthday is in the correct format useing regular expression
    matches = re.search(r"(\d{4})-(\d{2})-(\d{2})", birthday)
    if not matches:
        return False

    year, month, day = map(int, matches.groups())

    # check is date is in range
    try:
        date(year, month, day)
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    raise SystemExit(main())
