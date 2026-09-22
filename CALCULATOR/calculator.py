def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error : Division by zero" if b == 0 else a / b
def modulus(a, b): return a % b
def power(a, b): return a ** b
 
operations = {"1": add, "2": subtract, "3": multiply,
              "4": divide, "5": modulus, "6": power}
 
while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Modulus  6.Power  7.Exit")
    choice = input("Enter your choice : ")
 
    if choice == "7":
        print("Calculator closed.")
        break
 
    if choice in operations:
        try:
            a = float(input("Enter first number  : "))
            b = float(input("Enter second number : "))
            print("Result :", operations[choice](a, b))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    else:
        print("Invalid choice, try again.")
