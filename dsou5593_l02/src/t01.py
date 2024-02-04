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

s = Stack()

print("Is empty on an empty stack:", s.is_empty())

s.push(1)
s.push(2)
s.push(3)

print("Is empty on a non-empty stack:", s.is_empty())

print("Peek on a non-empty stack:", s.peek())

popped_value = s.pop()
print("Popped value:", popped_value)

print("Peek after pop:", s.peek())

print("Is empty after pop:", s.is_empty())

while not s.is_empty():
    print("Popped value:", s.pop())
