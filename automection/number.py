import random

def generate_indian_mobile_numbers(count):
    mobile_numbers = []
    for _ in range(count):
        # Indian mobile numbers start with 6, 7, 8, or 9 and have 10 digits
        first_digit = random.choice(['7', '8', '9'])
        remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        mobile_number = first_digit + remaining_digits
        mobile_numbers.append(mobile_number)
    return mobile_numbers

# Generate 150 random Indian mobile numbers
indian_mobile_numbers = generate_indian_mobile_numbers(1000)

# Print the generated numbers
for number in indian_mobile_numbers:
    print(number)