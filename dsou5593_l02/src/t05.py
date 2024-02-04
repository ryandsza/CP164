"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_food

stack = Stack()

with open('foods.txt', 'r') as fh:
    for line in fh:
        food = read_food(line)
        stack.push(food)

stack_test(stack)
