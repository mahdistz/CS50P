import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Define the regular expressions for matching the two formats
    format1_regex = r"(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)"
    format2_regex = r"(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)"

    # Try to match the input string with the regular expressions
    format1_match = re.match(format1_regex, s)
    format2_match = re.match(format2_regex, s)

    if format1_match:
        # Extract the matched groups
        hour1, minute1, period1, hour2, minute2, period2 = format1_match.groups()
        # Validate the extracted time values
        if not is_valid_time(hour1, minute1) or not is_valid_time(hour2, minute2):
            raise ValueError("Invalid time")

        # Convert the time to the 24-hour format
        hour1 = convert_to_24_hour_format(int(hour1), period1)
        hour2 = convert_to_24_hour_format(int(hour2), period2)

        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute1:02}"

    elif format2_match:
        # Extract the matched groups
        hour1, period1, hour2, period2 = format2_match.groups()

        # Validate the extracted time values
        if not is_valid_time(hour1, "00") or not is_valid_time(hour2, "00"):
            raise ValueError("Invalid time")

        # Convert the time to the 24-hour format
        hour1 = convert_to_24_hour_format(int(hour1), period1)
        hour2 = convert_to_24_hour_format(int(hour2), period2)

        return f"{hour1:02}:00 to {hour2:02}:00"

    else:
        # If the input formats don't match, raise a ValueError
        raise ValueError("Invalid input format")


def is_valid_time(hour, minute):
    hour = int(hour)
    minute = int(minute)

    if hour < 0 or hour > 12:
        return False
    elif minute < 0 or minute > 59:
        return False
    else:
        return True


def convert_to_24_hour_format(hour, period):
    if period == "AM" and hour == 12:
        hour = 0
    if period == "PM" and hour != 12:
        hour += 12

    return hour


if __name__ == "__main__":
    main()