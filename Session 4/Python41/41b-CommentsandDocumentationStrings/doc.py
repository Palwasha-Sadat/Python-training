def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    # This is a docstring, a multi-line string that provides documentation about the function.
    # It is typically used to explain the purpose of the function and how to use it.
  
    return None

# Print the docstring using the __doc__ attribute
print("Using __doc__:")
print(my_function.__doc__)

# Print the docstring using the help() function
print("Using help:")
help(my_function)
    