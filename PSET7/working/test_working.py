import pytest
from working import convert


def test_convert_valid_format1():
    result = convert("9:00 AM to 5:00 PM")
    assert result == "09:00 to 17:00"


def test_convert_valid_format2():
    result = convert("9 AM to 5 PM")
    assert result == "09:00 to 17:00"


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")


def test_convert_invalid_time():
    with pytest.raises(ValueError):
        convert("12:60 AM to 1:00 PM")


def test_convert_missing_minutes():
    result = convert("9 AM to 5 PM")
    assert result == "09:00 to 17:00"


def test_convert_missing_colon():
    with pytest.raises(ValueError):
        convert("900 AM to 5 PM")


def test_convert_invalid_format_to():
    with pytest.raises(ValueError):
        convert("12:00 AM  to  1:00 PM")