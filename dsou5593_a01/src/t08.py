"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

small, large, total, average = matrix_stats(matrix)

print("Smallest number:", small)
print("Largest number:", large)
print("Total:", total)
print("Average:", average)
