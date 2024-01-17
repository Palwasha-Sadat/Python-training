# Define lists for regions, sales, and employees
regions = ["North", "South", "East", "West"]
Sales = [30000, 20000, 40000, 35000]
employees = ["Alice", "Vera", "Flo", "Mel"]


# Uncomment the following code to print the names of employees
"""
for employee in employees:
    print(employee)
"""


employees.append("Joan")  # Add "Joan" to the list
employees.remove("Flo")  # Remove "Flo" from the list
employees.sort()  # Sort the list alphabetically


# Print the updated list of employees
for employee in employees:
    print(employee)
