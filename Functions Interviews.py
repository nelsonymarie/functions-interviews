def reverse_string(s: str) -> str:
    """
    Reverse a string using slicing.

    :param s: The string to be reversed
    :return: The reversed string
    """
    return s[::-1]
print(reverse_string("Hello World"))

# Function Definition: reverse_string
# Function Signature: def reverse_string(s: str) -> str:
#
# def is a keyword in Python used to define a function.
# reverse_string is the name of the function.
# s: str specifies that the function takes one parameter, s, and this parameter is expected to be a string (as indicated by the type hint str).
# -> str is a return type hint, indicating that this function returns a string.
# Docstring:
#
# Enclosed within triple quotes """, the docstring provides a description of the function.
# :param s: describes the parameter s.
# :return: describes what the function returns.
# Function Body:
#
# return s[::-1]
# This is where the core logic of the function resides.
# s[::-1] uses Python's slicing mechanism.
# In slicing, s[start:stop:step], start and stop define the range of the slice (which we omit, meaning it covers the entire string).
# The step part is -1, which means we go through the string in reverse.
# So, s[::-1] starts from the end of the string and steps back one character at a time, effectively reversing the string.
# Function Call: print(reverse_string("Hello World"))
# Calling the Function:
#
# reverse_string("Hello World") calls the reverse_string function with "Hello World" as the argument.
# The function processes this string, reversing it to "dlroW olleH".
# Printing the Result:
#
# print(...): The print function is used to output the result to the console.
# It takes the returned value from reverse_string("Hello World"), which is "dlroW olleH", and prints it out.
# When you run this entire code block, the print statement calls the reverse_string function with "Hello World", receives "dlroW olleH" in return, and then prints this reversed string to the console.