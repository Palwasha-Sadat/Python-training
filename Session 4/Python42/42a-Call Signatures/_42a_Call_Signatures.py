# Define a function to calculate the subtotal based on the order amount and sales tax rate
def subtotal(orderAmt, salesTax):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal

# Input for the first order
firstOrderAmount = input("Enter the order amount for the first order: ")
firstTax = input("Enter the sales tax rate for the first order: ")
firstOrderTotal = subtotal(firstOrderAmount, firstTax)

# Input for the second order
secondOrderAmount = input("Enter the order amount for the second order: ")
secondTax = input("Enter the sales tax rate for the second order: ")
secondOrderTotal = subtotal(secondOrderAmount, secondTax)

# Input for the third order
thirdOrderAmount = input("Enter the order amount for the third order: ")
thirdTax = input("Enter the sales tax rate for the third order: ")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

# Print the subtotal for each order
print("Your subtotal for the first order is %.2f" % firstOrderTotal)
print("Your subtotal for the second order is %.2f" % secondOrderTotal)
print("Your subtotal for the third order is %.2f" % thirdOrderTotal)

# Now, we're reusing the thirdOrderTotal variable and asking for a new sales tax rate for the third order
thirdTax = input("Enter your sales tax rate.")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

# Print the updated subtotal for the third order
print("Your subtotal for the third order with the new tax rate is %.2f" % thirdOrderTotal)

# Provide a default value of 0 for fourthOrderTotal
fourthOrderTotal = 0
print("Your subtotal for the fourth order is %.2f" % fourthOrderTotal)
