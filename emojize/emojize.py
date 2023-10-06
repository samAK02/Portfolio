import sys
import emoji

def main():
    response = input("Input:")
    out = emoji.emojize(response)
    print("Output:",out)

main()
