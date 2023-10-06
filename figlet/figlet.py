import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        rfont = random.choice(figlet.getFonts())
        response = input("Input: ")
        print("Output: ")
        print(figlet.renderText(response))

    elif (
        len(sys.argv) == 3
        and sys.argv[1] in ["-f", "--font"]
        and sys.argv[2] in figlet.getFonts()
    ):
        figlet.setFont(font=sys.argv[2])
        response = input("Input: ")
        print("Output:")
        print(figlet.renderText(response))

    else:
        sys.exit("invalid usage")


main()
