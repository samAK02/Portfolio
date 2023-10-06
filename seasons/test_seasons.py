from seasons import checking_bday
import pytest


def main():

    test_wrong_format()
    test_good_format()


def test_wrong_format():
    assert checking_bday("January 1, 1999") == None
    assert checking_bday("04/08/2023") == None
    assert checking_bday("12-11-2004") == None

def test_good_format():
    assert checking_bday("2023-08-03") == ("2023", "08", "03")


if __name__ == "__main__":
    main()
