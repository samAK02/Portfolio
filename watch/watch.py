import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search("<iframe(.)*><\/iframe>", s):
        matches = re.search(r"(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-z_A-Z_0-9]+)",s)
        if matches:
            str = matches.groups()
            return "https://youtu.be/" + str[3]


if __name__ == "__main__":
    main()