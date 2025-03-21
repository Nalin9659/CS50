def main():
    # Prompt user for input
    expression = input("Enter an arithmetic expression (x y z): ")
    
    # Split the input into parts
    x, operator, z = expression.split()
    
    # Convert x and z to integers
    x = int(x)
    z = int(z)
    
    # Perform the operation based on the operator
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        print("Invalid operator!")
        return
    
    # Print result formatted to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
