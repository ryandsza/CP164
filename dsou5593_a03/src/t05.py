"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

test_cases = [
    "racecar",
    "Otto",
    "Able was I ere I saw Elba",
    "hello",
    "1234",
    "A man, a plan, a canal, Panama!"
]

for string in test_cases:
    palindrome = is_palindrome_stack(string)
    print(f"'{string}' is a palindrome: {palindrome}")
