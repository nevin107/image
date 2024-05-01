
number = int(input("Enter a number: "))
sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number //= 10

# Print the sum of digits
print("Sum of digits:", sum)
