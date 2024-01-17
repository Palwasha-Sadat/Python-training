annualSales = 200000  # Define the annual sales amount

if annualSales >= 500000:
    print("Gold Customer")  # If sales are greater than or equal to 500,000, classify as Gold Customer
elif annualSales >= 300000:
    print("Silver Customer")  # If not Gold, but sales are greater than or equal to 300,000, classify as Silver Customer
elif annualSales >= 100000:
    print("Bronze Customer")  # If not Gold or Silver, but sales are greater than or equal to 100,000, classify as Bronze Customer
    #pass  # This line is commented out and has no effect on the program's behavior

print("Thank you for your business")  # Print a thank you message regardless of the customer's category
