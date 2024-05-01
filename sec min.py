# Sample strings
sample_strings = ['abc', 'string', 'go', 'coding']

# Process each sample string
for i in sample_strings:
    if len(i) >= 3:
        if i[-3:] == 'ing':
            result = i + 'ly'
        else:
            result = i + 'ing'
    else:
        result =i

    print(f"Sample String: '{i}' -> Expected Result: '{i}'")