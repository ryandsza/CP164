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
from functions import postfix

test_cases = [
    "12 5 -",
    "4 5 + 12 * 2 3 * -"
]

for expression in test_cases:
    answer = postfix(expression)
    print(f"Result of '{expression}': {answer}")
