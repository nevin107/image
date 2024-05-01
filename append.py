# Get input words from the user
words = input("Enter the words: ").split()

# Get input vowel letter from the user
vowel = input("Enter the vowel letter: ")

# Print the words starting with the given vowel
print("The words are:")
for word in words:
    if word.lower().startswith(vowel.lower()):
        print(word)
