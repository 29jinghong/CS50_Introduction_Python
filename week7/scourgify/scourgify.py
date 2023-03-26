import csv
import sys

def main():
    argc = len(sys.argv)

    if argc > 3:
        sys.exit("Too many command-line arguments")

    if argc < 3:
        sys.exit("Too few command-line arguments")

    befor = sys.argv[1]
    after = sys.argv[2]
    data = []
    if not befor.endswith(".csv") and after.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(befor) as file:
            f = csv.DictReader(file)
            for row in f:
                student = row
                name = student["name"]
                first, last = name.split(", ")
                house = student["house"]
                data.append({"first":first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("Dident find the file")

    with open(after, "w") as file:
        head = ["first", "last", "house"]
        write = csv.DictWriter(file, fieldnames=head)
        write.writeheader()
        for student in data:
            write.writerow(student)

if __name__ == "__main__":
    raise SystemExit(main())
