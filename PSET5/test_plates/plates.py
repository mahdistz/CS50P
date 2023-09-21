import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    special_chars = [".", " ", ",", ";", ":", "!", "@", "#", "$", "%", "^", "&", "*"]
    if 2 <= len(s) <= 6 and s[:2].isalpha():
        for char in s:
            if char not in special_chars:
                pass
            else:
                return False
        match = re.search(r"(\d+)$", s)
        if match:
            numbers = match.group(1)
            if len(numbers) > 1 and numbers[0] != "0":
                return True
        else:
            return True
    return False


if __name__ == "__main__":
    main()