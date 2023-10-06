from numb3rs import validate
import pytest

def main():
    test_non_valid_nums()
    test_len()



def test_non_valid_nums():
    assert validate(r"278.689.756.789") == False
    assert validate(r"-9.65.78.3") == False
    assert validate(r"cat.dog.bird.horse") == False

def test_len():
    assert validate(r"2.2") == False
    assert validate(r"24.35.65.7") == True
    assert validate(r"11.11.2.3.6.5.8") == False

if __name__ == "__main__":
    main()

