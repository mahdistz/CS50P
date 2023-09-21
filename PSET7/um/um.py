import re


def main():
    print(count(input("Text: ")))


def count(line):
    # Define the regex pattern to match "um" as a whole word
    pattern = r'\bum\b'

    # Find all matches of the pattern in the line (case-insensitive)
    matches = re.findall(pattern, line, re.IGNORECASE)

    # Return the count of matches
    return len(matches)


if __name__ == "__main__":
    main()