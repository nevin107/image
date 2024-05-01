# Given list of numbers
numbers = [10, 5, 7, 3, 15, 8, 20]

# Initialize min and max values with the first element of the list
minimum =numbers[0]
maximum =numbers[0]

# Iterate through the list to find minimum and maximum values
for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

# Print the minimum and maximum values
print("Minimum value:", minimum)
print("Maximum value:", maximum)
