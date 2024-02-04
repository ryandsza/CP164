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
from utilities import array_to_queue, queue_to_array, queue_test

source_list = [1, 2, 3, 4, 5]
target_list = []
queue = Queue()

print("Source list before:", source_list)
array_to_queue(queue, source_list)
print("Queue after array_to_queue:", list(queue))
queue_to_array(queue, target_list)
print("Target list after queue_to_array:", target_list)

# Test queue_test
a = [10, 20, 30, 40, 50]
queue_test(a)
