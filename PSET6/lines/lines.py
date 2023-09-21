import sys
import os

def count_code_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        return len(code_lines)


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) == 2 and sys.argv[1].endswith(".py") and not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")
elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    print(count_code_lines(sys.argv[1]))


