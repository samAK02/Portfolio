from working import update
import pytest

def main():

    test_format()
    test_hours()
    test_min()
    test_time()



def test_format():
    with pytest.raises(ValueError):
        update("9 AM - 5 PM")

def test_hours():
    with pytest.raises(ValueError):
        update("10 PM to 19 AM")

def test_min():
    with pytest.raises(ValueError):
        update("10:75 PM to 8:92 AM")

def test_time():
    assert update("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert update("9:00 AM to 5:00 PM") == "09:00 to 17:00"






if __name__ == "__main__":
    main()