import sys
import requests

BC = 38761.0833

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Is not a value")

    print(BC * bitcoin)
    
main()
