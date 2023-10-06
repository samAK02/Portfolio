from twttr import shorten
def main():
    test_lower_upper()
    test_numbers()


def test_lower_upper():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert("1234") == "1234"

def test_ponctuation():
    assert shorten(",.!?") == ",.!?"

if __name__ == "__main__":
    main()