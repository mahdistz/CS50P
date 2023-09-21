import pytest
from um import count

def test_count():
    # Test case where "um" appears once as a standalone word
    assert count("hello, um, world") == 1
    # Test case where "um" appears multiple times as a standalone word
    assert count("um, um, um") == 3
    # Test case where "um" appears as a substring of a word
    assert count("yummy") == 0
    assert count("UM, hum, HUm") == 1


