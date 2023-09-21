data = {}
while True:
    try:
        item = input().upper()
        if item not in data:
            data[item] = 1
        else:
            data[item] += 1
    except EOFError:
        sorted_data = sorted(data.items(), key=lambda x: x[0])
        for item in sorted_data:
            print(item[1], item[0], end="\n")
        break
