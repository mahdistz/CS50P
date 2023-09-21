def main():
    time = input("What time is it? ")
    output = convert(time)
    if 7.0 <= output <= 8.0:
        print("breakfast time")
    elif 12.0 <= output <= 13.0:
        print("lunch time")
    elif 18.0 <= output <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(int(minutes) / 60)
    return float(hours + minutes)


if __name__ == "__main__":
    main()
