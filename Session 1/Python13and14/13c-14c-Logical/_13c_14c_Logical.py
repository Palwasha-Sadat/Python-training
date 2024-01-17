# Assign values to variables
a = 15
b = 25
c = 15
d = 20

# Check if a is equal to c and b is not equal to c
print(a == c and b != c)  # True because a is equal to c (True) and b is not equal to c (True)

# Check if a is equal to b and b is equal to c
print(a == b and b == c)  # False because a is not equal to b (False)

# Check if a is equal to b or b is equal to c
print(a == b or b == c)  # False because a is not equal to b (False) and b is not equal to c (False)

# Check if a is not equal to b or b is equal to c
print(not a == b or b == c)  # True because a is not equal to b (True)



