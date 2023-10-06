def main():
    tweet = input("Input: ")
    tweet = shorten(tweet)
    print("Output: ",tweet)


def shorten(s):
    vowels = "aeiouAEIOU"
    result = []

    for i in s:
        if i not in vowels:
            result.append(i)
    return "".join(result)

if __name__ == "__main__":
    main()
