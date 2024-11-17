import re

def check_password_strength(password):
    feedback = []
    
    # Check length
    if len(password) < 12:
        feedback.append("Password should be at least 12 characters long.")
    
    # Check for uppercase, lowercase, digit, special character
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        feedback.append("Password should contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password should contain at least one special character.")
    
    # Check for common passwords
    common_passwords = ["123456", "password", "qwerty", "abc123"]
    if password in common_passwords:
        feedback.append("Password is too common and easily guessable.")
    
    if not feedback:
        return "Strong Password!"
    else:
        return "\n".join(feedback)

# Input from user
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print("\nFeedback on Password Strength:")
print(result)
