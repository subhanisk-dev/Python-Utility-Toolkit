import secrets
import string
 
def generate_otp(length=6, alphanumeric=False):
    # secrets is safer than random for OTPs and passwords
    characters = string.digits
    if alphanumeric:
        characters = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))
 
print("----- OTP GENERATOR -----")
length = int(input("Enter the OTP length: "))
choice = input("Do you want an alphanumeric OTP? (y/n): ").strip().lower()
 
otp = generate_otp(length, choice == "y")
 
print("Your OTP is :", otp)
print("This OTP is valid for 5 minutes. Do not share it with anyone.")
