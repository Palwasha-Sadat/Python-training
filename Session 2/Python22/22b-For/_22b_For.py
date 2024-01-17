# Define the initial annual sales goal
initialSalesGoal = 20000

# Define a multiplier for increasing the monthly sales goal
multiplier = 100

# Iterate through 12 months using a for loop
for monthlyGoal in range(12):
    # Calculate the monthly sales goal for each month
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
    
    # Print the calculated sales goal for the current month
    print("Your sales goal for month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))

# After the loop is finished, print a message to wish the person good luck with their sales goals
print("GOOD LUCK WITH YOUR GOALS.")




############## Exersice ##########################
"""
The ABC company needs a way to find the count of particular letters in their publications to ensure that there 
is a good balance. It seems that there have been complaints about overuse of the letter e. You need to create
a function to meet the requirements.

 1. function accept list of word from a file,
 and letter to search for.
 returns count of a particular letter in that list.
"""




