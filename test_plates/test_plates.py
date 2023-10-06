from plates import is_valid

def main():
    test_len()
    firstwo_letter()
    test_num()
    test_zero()



def test_len():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGH") == False

def firstwo_letter():
    assert is_valid("AS256") == True
    assert is_valid("12A") == False
    assert is_valid("AA") == True
    assert is_valid("2A") == False

def test_num():
    assert is_valid("AA2") == True
    assert is_valid("AA20A") == False
    assert is_valid("AZ45EE") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False



if __name__ == "__main__":
    main()