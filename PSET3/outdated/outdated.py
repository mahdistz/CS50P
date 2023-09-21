months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    date_input = input("Date: ")
    try:
        # month day, year
        if "," in date_input:
            m_d, y = date_input.split(",")
            m, d = m_d.split(" ")
            m = months.index(m) + 1

        # month/day/year
        elif "/" in date_input:
            m, d, y = date_input.strip().split("/")

        if int(m) > 12 or int(d) > 31:
                raise ValueError

    except Exception:
        pass

    else:
        print(f"{int(y)}-{int(m):02}-{int(d):02}")
        break