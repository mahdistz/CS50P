from validator_collection import validators

email_address = input("What's your email address? ")

try:
    result = validators.email(email_address)
    print("Valid")
except Exception:
    print("Invalid")