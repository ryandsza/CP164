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
from Queue_array import Queue

queue = Queue()

queue.insert(10)
queue.insert(20)
queue.insert(30)

removed_value = queue.remove()
print("Removed value:", removed_value)
print("Queue after removal:", list(queue))

peeked_value = queue.peek()
print("Peeked value:", peeked_value)
print("Queue after peek:", list(queue))
