from validator_collection import validators
import sys

def main():
    mail = input("What's your email adress? ")
    try:
        email_address = validators.email(mail)
        print("Valid")
    except:
        print("Invalid")








if __name__ == "__main__":
    main()
