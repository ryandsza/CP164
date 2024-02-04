"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_table
from Food import Food

with open('foods.txt', 'r') as file:
    foods = []
    for line in file:
        data = line.strip().split('|')
        name, origin, is_vegetarian, calories = data[0], int(
            data[1]), data[2] == 'True', int(data[3])
        food = Food(name, origin, is_vegetarian, calories)
        foods.append(food)

food_table(foods)
