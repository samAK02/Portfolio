def convert(Cword):
    snake_case = ""
    for i in Cword:
        if i.isupper():
            snake_case += "_" + i.lower()
        else:
            snake_case += i
    return snake_case.lstrip("_")

def main():
    word = input("camelCase: ")
    sword = convert(word)
    print("snake_case: ",sword)


main()
