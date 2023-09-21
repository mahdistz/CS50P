import random


def main():
    score = 0
    level = get_level()
    counter = 0

    while counter < 10:
        X = generate_integer(level)
        Y = generate_integer(level)
        answer = X + Y
        answers = []
        while True:
            num = input(f"{X} + {Y} = ")
            answers.append(num)
            if not num.isdigit():
                print("EEE")
            elif int(num) != int(answer):
                print("EEE")
                if len(answers) == 3:
                    print(f"{X} + {Y} = {answer}")
                    break
            elif int(num) == int(answer):
                if len(answers) == 1:
                    score += 1
                break

        counter += 1
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            break
    return int(level)


def generate_integer(level):
    if str(level) not in ["1", "2", "3"]:
        raise ValueError
    elif level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
