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
from utilities import array_to_pq, pq_to_array, priority_queue_test
from Priority_Queue_array import Priority_Queue

with open("foods.txt", "r") as file:
    food_data = [line.strip().split("|") for line in file.readlines()]

pq = Priority_Queue()

array_to_pq(pq, food_data)

priority_queue_test(food_data)

target_list = []

pq_to_array(pq, target_list)

print("Contents of the target list after pq_to_array:")
for food in target_list:
    print(food)
