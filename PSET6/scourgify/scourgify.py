import sys
import csv
import os



if len(sys.argv) == 1 or len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3 and not os.path.exists(sys.argv[1]):
    sys.exit(f"Could not read {sys.argv[1]}")
elif len(sys.argv) == 4:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    with open(sys.argv[1], "r", newline='') as input_file:
        reader = csv.DictReader(input_file)
        data = list(reader)

        for item in data:
            last, first = str(item['name']).split(",")
            house = item["house"]
            del item['name']
            del item['house']
            item["first"] = first.strip()
            item["last"] = last.strip()
            item["house"] = house

    with open(sys.argv[2], "w", newline='') as output_file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)