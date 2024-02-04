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
from utilities import array_to_stack

stack = Stack()

source = [1, 2, 3, 4, 5]

array_to_stack(stack, source)

print("Is stack empty after array_to_stack:", stack.is_empty())

print("Popped value from the stack:", stack.pop())
print("Popped value from the stack:", stack.pop())
print("Popped value from the stack:", stack.pop())
print("Popped value from the stack:", stack.pop())
print("Popped value from the stack:", stack.pop())

print("Is stack empty after popping all values:", stack.is_empty())
