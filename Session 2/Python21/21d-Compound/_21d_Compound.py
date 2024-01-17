# Define a variable 'annualSales' and assign the value 300,000 to it
annualSales = 300000

# Define a variable 'newCustomer' and assign the value False to it
newCustomer = False

# Check if 'annualSales' is greater than or equal to 500,000
if annualSales >= 500000:
    print("Gold Customer")
# If 'annualSales' is not greater than or equal to 500,000, check if it's greater than or equal to 300,000
elif annualSales >= 300000:
    print("Silver Customer")
# If 'annualSales' is not greater than or equal to 300,000, add a compound conditional statement
elif annualSales >= 100000 and newCustomer:
    print("Bronze Customer and first-time prize winner")
# If 'annualSales' is not greater than or equal to 100,000 and not a new customer, check if it's greater than or equal to 100,000
elif annualSales >= 100000:
    print("Bronze Customer")

# Print a thank you message
print("Thank you for your business")

# Comments added for each part of the code, including the customer classification based on 'annualSales' and the thank you message.
