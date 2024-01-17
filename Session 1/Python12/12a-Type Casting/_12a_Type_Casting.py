# Prompt the user to input the capital of Germany
capitalGuess = input("Where is the capital of Germany: ")

# Initialize the variable to keep track of the number of guesses
numberOfGuesses = 1

# Create a while loop that continues until the correct answer is guessed
while capitalGuess != "Berlin":
    # Increment the number of guesses
    numberOfGuesses += 1
    # Ask the user to guess again
    capitalGuess = input("Another guess: ")

# When the correct answer is guessed, print the result
print(f"Yes, {capitalGuess} is the capital of Hungary.")
print(f"Number of guesses: {numberOfGuesses}")
 
# f-string is a way to format strings in Python by including expressions inside curly braces {}