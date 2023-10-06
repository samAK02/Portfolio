def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)< 2 and len(s)>6:
        return False
    if contains_punctuation(s):
        return False
    if not first_two(s):
        return False
    if not has_valid_num(s):
        return False
    return True

def contains_punctuation(s):
    ponctuation = ["",",",";","?","!",".",":"]
    for i in s:
        if i in ponctuation:
            return True
    return False

def first_two(s):
    ftwo = s[:2]
    return ftwo.isalpha()

def has_valid_num(s):
    if s[-1].isdigit() and s[2:-1].isalnum() and s[2] != '0':
        return True
    return False

main()