# Define the size of the alphabet pattern
size = 5

# Iterate over each row
for i in range(size):
    # Print the first and last rows filled with asterisks
    if i == 0:
        print("*" * size)
    # Print the middle rows with a single asterisk
    else:
        print("*")

# Output:
# *****
# *
# *
# ****
# *
# *
# *****
