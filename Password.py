import string

# Evaluating password strength
def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    digits = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    characters = [upper_case, lower_case, digits, special]

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 15:
        score += 1

    score += sum(characters)

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score

# Input and result
password = input("Enter the password: ")
strength, score = password_strength(password)
print(f"Password strength: {strength} (Score: {score})")
