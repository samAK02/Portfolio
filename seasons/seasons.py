from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():

    bd = input("Birth Date: ")
    try:
        year, month, day = checking_bday(bd)
    except:
        sys.exit("Invalid Date")

    date_of_birth = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - date_of_birth
    minutes = diff.days * 24 * 60
    minutes_str = p.number_to_words(minutes, wantlist=False, andword = "")
    print(minutes_str.capitalize() + " minutes")


def checking_bday(bd):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",bd):
        year,month,day = bd.split("-")
        return year,month,day


if __name__ == "__main__":
    main()