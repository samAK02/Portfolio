from um import count
import pytest

def main():
    test_sep_um()
    test_wrong_way()
    test_cap()

def test_sep_um():
    assert count("hello, um, world") == 1
    assert count ("um, hello, um.., what is um you name?") == 3

def test_wrong_way():
    assert count("yummi") == 0
    assert count("summary") == 0

def test_cap():
    assert count("Um hi") == 1


if __name__ == "__main__":
    main()