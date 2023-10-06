import csv
import sys
from tabulate import tabulate

# Here the main program will be executed

def main():
    check_format()

    data = []

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(data[1:], headers = data[0], tablefmt="grid"))

#checking if the format is correct:

def check_format():
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        if len(sys.argv) < 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()