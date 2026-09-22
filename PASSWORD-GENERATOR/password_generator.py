import secrets
import string
 
def generate_password(length):
    if length < 4:
        return "Password length must be at least 4"
 
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"
    all_chars = lower + upper + digits + symbols
 
    # guarantee at least one character from every category
    password = [secrets.choice(lower), secrets.choice(upper),
                secrets.choice(digits), secrets.choice(symbols)]
 
    password += [secrets.choice(all_chars) for _ in range(length - 4)]
 
    secrets.SystemRandom().shuffle(password)
    return "".join(password)
 
n = int(input("Enter required password length: "))
print("Generated password :", generate_password(n))
