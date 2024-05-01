# Input integer
N = int(input("Enter an integer: "))

# Check the conditions and print the corresponding message
if N % 2 != 0:
    print("Weird")
elif N >= 5 and N <= 11:
    print("Not Weird")
elif N >= 13 and N <= 35:
    print("Weird")
elif N > 36:
    print("Not Weird")
