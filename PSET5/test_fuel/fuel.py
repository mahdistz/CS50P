def main():
    fraction = input("Fraction: ")
    int_number = convert(fraction)
    result = gauge(int_number)
    print(result)


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round((x / y) * 100)



def gauge(percentage):
    if 1 < percentage < 99:
        return str(percentage) + "%"
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"




if __name__ == "__main__":
    main()


