region = "West"  # Set the variable 'region' to "West"
annualSales = 500000  # Set the variable 'annualSales' to 500,000
firstName = "Tony"  # Set the variable 'firstName' to "Tony"

# Check the annual sales to determine the customer category
if annualSales >= 500000:
    print("Gold Customer")  # If annual sales are at least 500,000, print "Gold Customer"
elif annualSales >= 300000:
    print("Silver Customer")  # If not Gold, but annual sales are at least 300,000, print "Silver Customer"
elif annualSales >= 100000:
    print("Bronze Customer")  # If not Gold or Silver, but annual sales are at least 100,000, print "Bronze Customer"
    print("Thank you for your business")  # This message is printed for Bronze Customers

# Print additional information about the customer
print(f"Your sales representative is {firstName}, you are in the {region} region, and you had {annualSales} in sales last year. Thanks!")
