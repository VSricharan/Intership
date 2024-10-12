# Function to perform the calculations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation"

# Main program loop
def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Taking user inputs
        operation = input("Choose an operation (1-5): ")
        
        if operation == '5':
            print("Goodbye!")
            break

        # Ensure valid operation is chosen
        if operation in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                # Perform calculation and display the result
                result = calculate(num1, num2, operation)
                print(f"The result is: {result}")
            
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please choose a valid operation.")
        
if __name__ == "__main__":
    main()