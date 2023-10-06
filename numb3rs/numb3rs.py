import re
import sys

def main():
    ip = input("IPv4 Adress: ")
    if validate(ip):
        sys.exit("True")

    if not validate(ip):
        sys.exit("False")


def validate(ip):
    if re.search(r"^[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+$", ip):
        nums = ip.split(".")
        for i in nums:
            if int(i) < 0 or int(i) >255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
