
def count_vowels(in_string):
    """Returns the number of vowels contained in `in_string`."""
    num_vowels = 0
    vowels = "aeiouAEIOU"

    for char in in_string:
        if char in vowels:
            num_vowels += 1  # equivalent to num_vowels = num_vowels + 1
    return num_vowels

# Example usage:
input_string = "Hello, World!"
result = count_vowels(input_string)
#print("Number of vowels:", result)

# https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Functions.html


"""
Write a function named count_even.
 It should accept one input argument, named numbers, 
 which will be an iterable containing integers. Have the function return the number of even-valued integers 
 contained in the list. Include a reasonable docstring.
"""


















def count_even(numbers):
    """
    Count the number of even-valued integers in the input iterable.

    Args:
    numbers (iterable of int): An iterable containing integers.

    Returns:
    int: The count of even-valued integers in the input iterable.
    """
    num_even = 0

    for num in numbers:
        if num % 2 == 0:
            num_even += 1

    return num_even
numbers_list = [1, 2, 3, 4, 5, 6, 7]
result = count_even(numbers_list)
print("Number of even integers:", result)

