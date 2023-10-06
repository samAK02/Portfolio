"""def main():

    greeting = input("Greeting: ")
    value_to_print = value(greeting)
    print(f'${value_to_print}')

def value(greeting):

    greeting = greeting.lower().strip()

    if 'hello' in greeting:
        return 0
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()"""


def main():
    salutation = input("Greetings: ")
    money = greetings(salutation)
    print(f"${money}")



def greetings(s):

    s = s.lower().strip()
    if "hello" in s:
        money = 0
    elif "h" == s[0]:
        money = 20
    else:
        money = 100
    return money

main()