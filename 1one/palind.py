def is_palindrome(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Check if the string is equal to its reverse
    if number_str == number_str[::-1]:
        return True
    else:
        return False

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome and print the result
if is_palindrome(number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
