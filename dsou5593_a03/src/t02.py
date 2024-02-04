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
from Stack_array import Stack

source1 = Stack()
source2 = Stack()

for i in range(5, 0, -1):
    source1.push(i)

for i in range(6, 11):
    source2.push(i)

target = Stack()
target.combine(source1, source2)

print("Combined Stack:")
while not target.is_empty():
    print(target.pop())
