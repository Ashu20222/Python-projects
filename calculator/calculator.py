def calculator(operation, num1, num2):
     
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        return "Invalid operator"
    
    return result

# Get the operation from the user
operation = input("What operation would you like to perform? (+, -, *, /): ")

# Get the two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

 
result = calculator(operation, num1, num2)
print(result)
