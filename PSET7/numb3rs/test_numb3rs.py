from numb3rs import validate

def test_validate_ip_address():
    # Valid IPv4 address
    assert validate("192.168.0.1") == True

    # Invalid IP address (missing octet)
    assert validate("192.168.0") == False

    # Invalid IP address (extra octet)
    assert validate("192.168.0.1.2") == False

    # Invalid IP address (first byte is in range)
    assert validate("255.256.0.1") == False

    # Invalid IP address (letters in IPv4 octet)
    assert validate("192.168.ab.1") == False