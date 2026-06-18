import re

def check_password_strength(password):

    # few weak patterns
    common_patterns = ["password", "123", "qwerty", "admin"]

    for pattern in common_patterns:
        if pattern in password.lower():
            return "❌ Weak Password (Common Pattern)"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*" for c in password)

    # Count how many types are present
    types = sum([has_upper, has_lower, has_digit, has_symbol])

    # Only one type → Weak
    if types == 1:
        return "❌ Weak Password"

    # 2 or 3 types → Medium
    elif types == 2 or types == 3:
        return "👍 Medium Password"

    # All 4 types → Strong
    elif types == 4:
        return "✅ Strong Password"

    else:
        return "❌ Weak Password"


# main

print("🔐 Password Strength Checker")

password = input("Enter your password: ")

result = check_password_strength(password)

print("Result:", result)