import re

def is_camel_case(string):
    return bool(re.match(r'^[a-z]+(?:[A-Z][a-z]*)*$', string))

def camel_to_snake(string):
    # Add an underscore before any uppercase letter, then convert the entire string to lowercase
    snake_case = re.sub(r'([A-Z])', r'_\1', string).lower()
    return snake_case

text = input("camelCase: ")
if is_camel_case(text):
    snake_text = camel_to_snake(text)
    print(f"snake_case: {snake_text}")
else:
    print(f"snake_case: {text}")