# Accept the input sentence from the user
sentence = input("Enter a sentence: ")

# Initialize variables to count letters and digits
num_letters = 0
num_digits = 0

# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is a letter
    if char.isalpha():
        num_letters += 1
    # Check if the character is a digit
    elif char.isdigit():
        num_digits += 1

# Print the count of letters and digits
print("LETTERS", num_letters)
print("DIGITS", num_digits)
