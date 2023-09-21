while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        if x and y:
            result = float(int(x) / int(y))
            if 0 <= result <= 0.01:
                print("E")
                break
            elif 0.99 <= result <= 1.0:
                print("F")
                break
            elif 0.01 <= result <= 0.99:
                print(str(round(result * 100)) + "%")
                break
    except (ValueError, ZeroDivisionError):
        pass
