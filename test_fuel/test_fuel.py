from fuel import convert, gauge
import pytest

def main():
    test_correct_input()
    test_zero_division()
    Value()


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")


def test_correct_input():
    assert convert("1/2") == 50 and gauge(50) == ("50%")
    assert convert("1/100") == 1 and gauge(1) == ("E")
    assert convert("99/100") == 99 and gauge(99) == ("F")


def Value():
    with pytest.raises(ValueError):
        convert("hi/mark")

if __name__ == "__main__":
    main()
