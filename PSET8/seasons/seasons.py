from datetime import datetime,date
import re
import inflect
import sys


def age_in_minutes(date_of_birth):
    y, m, d = date_of_birth.split("-")
    if int(d) > 30 or int(m) > 12:
        raise ValueError
    birth_datetime = datetime.strptime(date_of_birth, '%Y-%m-%d')
    current_datetime = datetime(date.today().year, date.today().month, date.today().day)
    age = current_datetime - birth_datetime
    age_in_minutes = round(age.total_seconds() / 60)
    return age_in_minutes


def main():
    birthday = input("Date of Birth: ")
    if not re.match(r"(\d{4})-(\d{1,2})-(\d{1,2})", birthday):
        sys.exit("Invalid date")

    age = age_in_minutes(birthday)
    result_in_words = inflect.engine().number_to_words(age)
    result = result_in_words.replace(result_in_words.split(",")[0],
     result_in_words.split(",")[0].capitalize()).replace(" and ", " ")
    print(result, end=" minutes\n")

if __name__ == "__main__":
    main()


