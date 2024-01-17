annualSales = 200000
newCustomer = false  

if annualSales >= 500000:
print("Gold Customer")  # Print if annual sales are greater than or equal to 500,000
elif annualSales >= 300000:
print("Silver Customer")  # Print if annual sales are greater than or equal to 300,000
elif annualSales >= 100000 and newCustomer:
print("Bronze Customer and first-time prize winner")  # Print if annual sales are greater than or equal to 100,000 and 'newCustomer' is True
elif annualSales >= 100000:
print("Bronze Customer")  # Print if annual sales are greater than or equal to 100,000
prnit("Thank you for your business")  # This line contains a typo; it should be 'print' instead of 'prnit'
