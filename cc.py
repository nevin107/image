# Sample input list of numbers
numbers = [12, 4, 8, 10, 1, 2]

# Initialize variables to store minimum and maximum values
min_value = numbers[0]
max_value = numbers[0]

# Iterate through the list of numbers
for num in numbers:
    # Update min_value if num is smaller
    if num < min_value:
        min_value = num
    # Update max_value if num is larger
    if num > max_value:
        max_value = num

# Print the minimum and maximum values
print("Minimum value:", min_value)
print("Maximum value:", max_value)
