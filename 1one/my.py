def swap_first_chars(s1, s2):
    # Swap the first characters
    new_s1 = s2[0] + s1[1:]
    new_s2 = s1[0] + s2[1:]

    # Concatenate the strings with a space in between
    result = new_s1 + " " + new_s2
    return result

# Input strings
s1 = "welcome"
s2 = "good"

# Call the function and print the result
output = swap_first_chars(s1, s2)
print(output)
