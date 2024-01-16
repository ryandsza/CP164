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
from Food_utilities import read_foods, get_vegetarian

file_path = "foods.txt"
with open(file_path, 'r') as file_variable:
    foods_list = read_foods(file_variable)

vegetarian_foods = get_vegetarian(foods_list)
for food in vegetarian_foods:
    print(food)
