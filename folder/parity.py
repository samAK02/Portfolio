def main():
    x = int(input("what is the value of x? \n"))
    if is_even(x):
        print("the number is even")
    else:
        print("the number is odd")


def is_even(a):
    return a % 2 == 0


main()
