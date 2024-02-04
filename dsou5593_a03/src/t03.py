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
from functions import stack_reverse
from Stack_array import Stack

sample_stack = Stack()

for i in range(1, 6):
    sample_stack.push(i)

stack_reverse(sample_stack)

print("Reversed Stack:")
while not sample_stack.is_empty():
    print(sample_stack.pop())
