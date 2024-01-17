"""# Prompt the user to enter the capital of Latvia
capitalGuess = input("What is the capital of Latvia? ")
numberOfGuesses = 1  # Initialize the number of guesses to 1

# Start a loop to allow the user to make multiple guesses
while capitalGuess != "Riga":
    numberOfGuesses = numberOfGuesses + 1  # Increment the number of guesses
    if numberOfGuesses > 3:
        print("You guessed incorrectly three times. Game over.")
        break  # If the user exceeds three incorrect guesses, end the game
    capitalGuess = input("Guess again. ")  # Prompt the user to guess again

# The following code is executed when the user either guesses correctly or runs out of attempts
else:
    print("You guessed it. Riga is the capital of Latvia. It took you " + str(numberOfGuesses) + " guesses.")
"""

x = 3
y = 4
average = x + y / 0
print(average)
    
   