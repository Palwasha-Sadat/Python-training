# Define the initial annual sales goal
initialSalesGoal = 20000

# Define a multiplier for increasing the monthly sales goal
multiplier = 100

# Iterate through 12 months using a for loop (starting from month 1)
for monthlyGoal in range(1, 12):
    # Check if the current month is month 6
    if monthlyGoal == 6:
        # If it's month 6, add a print statement to inform there's no goal for this month
        print("No goal for month 6")
        continue  # Skip the rest of the loop for month 6 and continue to the next iteration
    
    # Calculate the monthly sales goal for other months
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
    
    # Print the calculated sales goal for the current month
    print("Your sales goal for month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))

# After the loop is finished, print a message to wish the person good luck with their sales goals
print("Good luck with your goals.")
