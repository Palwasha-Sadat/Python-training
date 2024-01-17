import random

# Run this five times:
for _ in range(5):
    guess = int(input("Enter a number between 1 and 10: "))
    randNum = random.randint(1, 10)  # Generate a random number between 1 and 10
    if guess == randNum:
        print("We matched!")
        break
    else:
        print("We did not match. Try again")

# Generate a random number between 1 and 10 (inclusive)
print(random.randint(1, 10))

# Generate a random sample of 5 numbers from the range [0, 99]
print(random.sample(range(100), 5))

cars = ["sedan", "SUV", "crossover", "truck"]

# Choose a random element from the 'cars' list
print(random.choice(cars))

# Shuffle the 'cars' list randomly
random.shuffle(cars)
print(cars)


"""import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_elements = random.sample(my_list, 3)

print("Sampled elements:", sampled_elements)"""


###################### Exersice##########################
"""
You are writing code that generates a random integer with a minimum value of 5 and a maximum value of 11.
Which two functions should you use? Each correct answer presents a complete solution. (Choose two.)

A. random.randint(5, 12)
B. random.randint(5, 11)
C. random.randrange(5, 12, 1)
D. random.randrange(5, 11, 1)
"""

######### solution ###########
"""
1. randint: starting number and stoping numbers are inclusive.
2. randrange:start: The starting point of the range (inclusive).
stop: The stopping point of the range (exclusive). This means that the range includes 
all integers from start up to, but not including, stop.
step (optional): The step value, which determines the increment between numbers.
If not provided, the default step is 1.

"""
import random

random_number = random.randint(5, 11)
random_numberr = random.randrange(5,12,1)
print(random_numberr)


