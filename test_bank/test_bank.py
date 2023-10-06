from bank import value

def main():
    test_hello()
    test_h_word()
    test_is_not()


def test_hello():
    assert value("hello") == 0
    assert value("Hello Sam") == 0
    assert value("HeLLo")== 0

def test_h_word():
    assert value('hey')== 20
    assert value('hi there') == 20

def test_is_not():
    assert value("bonjour") == 100
    assert value('goodbye') == 100

