import random


def main():
    cpt = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level)
        r = maths_prob(x, y)
        if r == True:
            cpt += 1

    print("score: ", cpt)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [3, 2, 1]:
                break
        except:
            pass
    return n


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


def maths_prob(x, y):
    try_cpt = 1
    while try_cpt <= 3:
        try:
            resp = int(input(f"{x} + {y} = "))
            if resp == (x + y):
                return True
            else:
                print("EEE")
                try_cpt += 1
        except:
            print("EEE")
            try_cpt += 1

    print(f"{x} + {y} = {x+y}")


if __name__ == "__main__":
    main()
