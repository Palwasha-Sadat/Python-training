# Define a function to calculate the subtotal based on the order amount and an optional sales tax rate (default is 0.0)
def subtotal(orderAmt, salesTax=0.0):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal

# Define a function to generate an order message
def orderMsg(orderNumber, subtotal):
    return f"Your subtotal for the {orderNumber} order is ${subtotal:.2f}"

# Calculate subtotals for the first and second orders
firstOrderTotal = subtotal(300)
secondOrderTotal = subtotal(400, 0.06)

# Input for the third order, specifying the order amount and sales tax rate
thirdOrderAmount = input("What was the order amount? ")
thirdTax = input("Enter your sales tax rate (as a decimal): ")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

# Calculate the subtotal for the fourth order
fourthOrderTotal = subtotal(800)

# Generate and print order messages for each order
print(orderMsg("first", firstOrderTotal))
print(orderMsg("second", secondOrderTotal))
print(orderMsg("third", thirdOrderTotal))
print(orderMsg("fourth", fourthOrderTotal))
