import re

def password_strength_checker(password):
    """
    Checks the strength of a given password.

    Args:
        password (str): The password to check.

    Returns:
        dict: A dictionary containing the password strength results.
    """
    results = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'special_chars': False
    }

    # Check password length
    if len(password) >= 8:
        results['length'] = True

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        results['uppercase'] = True

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        results['lowercase'] = True

    # Check for numbers
    if re.search(r"\d", password):
        results['numbers'] = True

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        results['special_chars'] = True

    # Calculate password strength
    strength = 0
    for value in results.values():
        if value:
            strength += 1

    # Map strength to a level (0-5)
    levels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong', 'Very Strong']
    level = levels[strength]

    return {
        'results': results,
        'strength': strength,
        'level': level
    }

# Example usage:
password = input("Enter a password: ")
results = password_strength_checker(password)

print("Password Strength Results:")
print("---------------------------")
for key, value in results['results'].items():
    print(f"{key.capitalize()}: {'Yes' if value else 'No'}")

print(f"\nPassword Strength: {results['strength']}/5")
print(f"Password Level: {results['level']}")