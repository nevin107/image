# Input number
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Calculate factorial using while loop
while num > 1:
    factorial *= num
    num -= 1

# Print the factorial
print("Factorial:", factorial)


