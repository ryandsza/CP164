"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(30)
pq.insert(20)
pq.insert(40)

peeked_value = pq.peek()

print("Peeked value:", peeked_value)
