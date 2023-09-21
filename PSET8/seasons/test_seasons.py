from seasons import age_in_minutes
import pytest


def test_age_in_minutes():
    # Test case where birthday in not coorect
    with pytest.raises(ValueError):
        age_in_minutes("2000-13-12")

    # Test case where input is in valid format
    assert age_in_minutes("2000-01-01") == 12463200  # Assuming 1 year = 52560 minutes