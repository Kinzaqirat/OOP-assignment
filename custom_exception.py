class InvalidAge(Exception):
    """Age is less than 18"""

def check_age(age):
    if age < 18:
        raise InvalidAge("Age must be 18 or older")
    else:
        print('Access geanted')

try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except InvalidAge as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid number.")