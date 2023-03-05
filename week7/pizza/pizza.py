import csv
import sys
from tabulate import tabulate


def main():
    argc = len(sys.argv)

    if argc > 2:
        sys.exit("Too many command-line arguments")

    if argc < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                rows.append(row)
            print(tabulate(rows[1:], rows[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

