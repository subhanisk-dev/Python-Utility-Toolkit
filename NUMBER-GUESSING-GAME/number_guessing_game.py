import random
 
low, high = 1, 100
secret = random.randint(low, high)
max_attempts = 7
attempts = 0
 
print("I have selected a number between", low, "and", high)
print("You have", max_attempts, "attempts to guess it.")
 
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess : "))
    except ValueError:
        print("Please enter a valid number.")
        continue
 
    attempts += 1
 
    if guess == secret:
        print("Correct! You guessed it in", attempts, "attempts.")
        break
    elif guess < secret:
        print("Too low.  Attempts left :", max_attempts - attempts)
    else:
        print("Too high. Attempts left :", max_attempts - attempts)
else:
    print("Out of attempts. The number was", secret)
