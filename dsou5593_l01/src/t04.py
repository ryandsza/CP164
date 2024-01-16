"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_food

sample_data = "Spanakopita|5|True|260"
left_food = read_food(sample_data)
print(left_food)
