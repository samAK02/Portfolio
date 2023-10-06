import csv
import sys

#the main program:

def main():
    check_command_line()
    students = []

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_splitted = row["name"].split(",")
                students.append(
                    {
                        "first name": name_splitted[1].lstrip(),
                        "last name": name_splitted[0].lstrip(),
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    try:
        with open(sys.argv[2], "w") as cfile:
            writer = csv.DictWriter(
                cfile, fieldnames=["first name", "last name", "house"]
            )
            writer.writerow(
                {"first name": "first name", "last name": "last name", "house": "house"}
            )
            for row in students:
                writer.writerow(
                    {
                        "first name": row["first name"],
                        "last name": row["last name"],
                        "house": row["house"],
                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[2]}")


# again checking if the command line is ok

def check_command_line():

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    else:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
