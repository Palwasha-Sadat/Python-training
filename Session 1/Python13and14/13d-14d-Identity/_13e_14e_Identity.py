a = 3
b = a

northItems = ["Rain gear", "Snow shoes"]
eastItems = ["Rain gear", "Snow shoes"]

# Check if a is equal to b
print(a == b)  # True because a is equal to b (True)

# Check if a is the same object as b (identity check)
print(a is b)  # True because a and b refer to the same object in memory (True)

# Check if the lists northItems and eastItems have the same contents
print(northItems == eastItems)  # True because both lists have the same contents (True)

# Check if the lists northItems and eastItems are the same object
print(northItems is eastItems)  # False because they are different objects in memory (False)

# Exercise description
"""
Exercise:

Evaluate this line of code:

numList = [1, 2, 3, 4, 5]
alphaList = [4, 6, 7, 8, 9]
print(numList is alphaList)
print(numList == alphaList)

numList = alphaList
print(numList is alphaList)
print(numList == alphaList)
"""
