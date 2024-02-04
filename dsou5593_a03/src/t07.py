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
from functions import stack_maze

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': [],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F', 'X'],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}

path = stack_maze(maze)

print("Path to the exit:")
print(path)
