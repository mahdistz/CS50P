from tabulate import tabulate
import sys
import csv
import os


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
elif len(sys.argv) == 2 and sys.argv[1].endswith(".csv") and not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")
elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        headers = rows[0]
        data = rows[1:]
        print(tabulate(data, headers=headers, tablefmt='grid'))


