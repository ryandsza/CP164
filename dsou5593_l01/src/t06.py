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
from Food_utilities import write_foods, read_foods

with open('foods.txt', 'r') as file:
    foods_list = read_foods(file)

with open('new_foods.txt', 'w') as new_file:
    write_foods(new_file, foods_list)
