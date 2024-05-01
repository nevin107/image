# Get words from the user
words = input("Enter the words: ").split()

# Get the vowel letter from the user
vowel = input("Enter the vowel letter: ").lower()

# Display the words starting with the given vowel
print("The words are:")
for word in words:
    if word.lower().startswith(vowel):
        print(word)
