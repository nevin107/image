# Initialize an empty list to store the input numbers
numbers = []

# Read 10 integer numbers as input and store them in the list
for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Initialize an empty list to store the multiples of both 2 and 8
multiples_of_2_and_8 = []

# Iterate through the list of numbers and find the multiples of both 2 and 8
for num in numbers:
    if num % 2 == 0 and num % 8 == 0:
        multiples_of_2_and_8.append(num)

# Display the multiples of both 2 and 8
print("Numbers that are multiples of both 2 and 8:", multiples_of_2_and_8)
