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
from utilities import stack_to_array
from Stack_array import Stack

stack = Stack()


stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

target = []

stack_to_array(stack, target)

print("Change the items in the target list after using stack_to_array:", target)

print("Is stack empty after stack_to_array:", stack.is_empty())
