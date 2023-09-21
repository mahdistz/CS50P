from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100