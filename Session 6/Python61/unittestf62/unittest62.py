import unittest  # Import the unittest module for writing and running test cases

# A simple function to add two numbers
def add(a, b):
    return a + b

# Create a test case class that inherits from unittest.TestCase
class TestAddition(unittest.TestCase):
    
    # Test if the addition function works as expected
    def test_addition(self):
        result = add(2, 3)  # Call the add function with arguments 2 and 3 and store the result
        # Use assertEqual to check if the result is equal to the expected value (5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()  # Run the tests if the script is executed




################  assertTrue() / assertFalse() ###########

"""import unittest  # Import the unittest module for writing and running test cases

# A simple function to check if a number is even
def is_even(number):
    return number % 2 == 0  # Check if the number is even by using the modulo operator

# Create a test case class that inherits from unittest.TestCase
class TestEvenNumber(unittest.TestCase):
    
    # Test if a number is even using assertTrue
    def test_is_even(self):
        self.assertTrue(is_even(4))  # Passes because 4 is an even number
        self.assertTrue(is_even(0))  # Passes because 0 is an even number
        self.assertTrue(is_even(-2))  # Passes because -2 is an even number
        self.assertFalse(is_even(7))  # Fails because 7 is not an even number
        self.assertFalse(is_even(-1))  # Fails because -1 is not an even number

if __name__ == '__main__':
    unittest.main()  # Run the tests if the script is executed
"""

################## self.assertIn ############################
"""import unittest  # Import the unittest module for writing and running test cases

class TestAssertions(unittest.TestCase):
    
    def test_in_list(self):
        fruits = ["apple", "banana", "cherry"]
        self.assertIn("apple", fruits)  # Passes because "apple" is in the list.
        self.assertIn("grape", fruits)  # Fails because "grape" is not in the list.

    def test_in_string(self):
        sentence = "This is a sample sentence."
        self.assertIn("sample", sentence)  # Passes because "sample" is in the string.
        self.assertIn("hello", sentence)   # Fails because "hello" is not in the string.

    def test_in_set(self):
        colors = {"red", "blue", "green"}
        self.assertIn("green", colors)  # Passes because "green" is in the set.
        self.assertIn("yellow", colors)  # Fails because "yellow" is not in the set.

if __name__ == '__main__':
    unittest.main()  # Run the tests if the script is executed"""

#############################################################################3

