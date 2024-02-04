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


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()

    while not source1.is_empty() or not source2.is_empty():
        if not source2.is_empty():
            target.push(source2.pop())
        if not source1.is_empty():
            target.push(source1.pop())

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    temp_stack = Stack()

    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    cleaned_string = ""
    for char in string:
        if char.isalnum():
            cleaned_string += char.lower()

    left = 0
    right = len(cleaned_string) - 1

    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    return True


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    tokens = string.split()

    for token in tokens:
        if token in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = eval(f"{operand1} {token} {operand2}")
            stack.push(result)
        else:
            stack.push(float(token))
    return stack.pop()


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()

    visited = set()

    start = 'Start'
    stack.push(start)

    while not stack.is_empty():
        current_point = stack.pop()

        if current_point == 'X':
            return list(visited)
        visited.add(current_point)

        branches = maze.get(current_point, [])
        for branch in branches:
            if branch not in visited:
                stack.push(branch)
    return None
