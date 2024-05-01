# Get input from the user
initial_amount = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the rate as a %: "))

# Calculate final amount
final_amount = initial_amount * (1 + interest_rate / 100) ** years

# Calculate interest earned
interest_earned = final_amount - initial_amount

# Display the investment report
print("\nInvestment Report:")
print("Initial Amount: $", format(initial_amount, '.2f'))
print("Number of Years:", years)
print("Interest Rate: ", interest_rate, "%")
print("Final Amount: $", format(final_amount, '.2f'))
print("Interest Earned: $", format(interest_earned, '.2f'))
