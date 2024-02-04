"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID:      169065593
Email:   dsou5593@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""

from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in range(len(source)):
        stack.push(source.pop())

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        target.insert(0, stack.pop())
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    stack = Stack()

    print(f"The stack is empty: {stack.is_empty()}")

    while len(source) > 0:
        stack.push(source.pop())

        print(f"The stack is empty: {stack.is_empty()}")

    while not stack.is_empty():
        print(f"Element to remove is {stack.peek()}!! {stack.pop()}")

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in source:
        queue.insert(value)
    source.clear()


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    print("Queue empty?", q.is_empty())

    for value in a:
        q.insert(value)
    print("Queue after insert:", list(q))

    if not q.is_empty():
        removed_value = q.remove()
        print("Remove:", removed_value)
    else:
        print("Removing from an empty queue is not possible")

    if not q.is_empty():
        removed_value = q.remove()
        print("Removed:", removed_value)
    else:
        print("Removing from an empty queue is not possible")

    if not q.is_empty():
        peek_value = q.peek()
        print("Peek at front of queue (non-empty queue):", peek_value)
    else:
        print("Cannot peek at an empty queue")

    if not q.is_empty():
        peek_value = q.peek()
        print("Peek at empty queue:", peek_value)
    else:
        print("Cannot peek at an empty queue")

    print("Length of queue:", len(q))

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in source:
        pq.insert(value)
    source.clear()


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    if len(a) > 0:
        for value in a:
            pq.insert(value)
        print("Priority Queue after insert:", list(pq))

        print("Priority queue empty?", pq.is_empty())
        print("Peek at priority queue:", pq.peek())

        while not pq.is_empty():
            print("Remove:", pq.remove())

        print("Priority queue empty now?", pq.is_empty())
    else:
        print("Nothing to test for non-empty priority queue.")

    print("Test empty priority queue:")
    print("Priority queue empty?", pq.is_empty())
    if not pq.is_empty():
        print("Peek at priority queue:", pq.peek())
    else:
        print("Cannot peek at an empty priority queue.")

    if not pq.is_empty():
        print("Attempting to remove from empty priority queue...")
        print("Remove:", pq.remove())
    else:
        print("Cannot remove from an empty priority queue.")

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        llist.append(source.pop(0))
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.append(llist.pop(0))
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print("Appending:")
    for item in source:
        lst.append(item)
    print("List after appending:", lst)

    print("\nInserting elements:")
    for i, item in enumerate(source):
        lst.insert(i, item)
    print("List after inserting:", lst)

    print("\nRemoving elements:")
    while not lst.is_empty():
        removed_item = lst.remove(0)
        print("Removed item:", removed_item)
        print("List after removal:", lst)

    print("\nCounting elements:")
    for item in source:
        count = lst.count(item)
        print(f"Count of {item}: {count}")

    print("\nAppending elements again:")
    for item in source:
        lst.append(item)
    print("List after appending again:", lst)

    print("\nFinding elements:")
    for item in source:
        index = lst.find(item)
        print(f"Index of {item}: {index}")

    print("\nFinding maximum:")
    max_item = lst.max()
    print("Maximum item:", max_item)

    print("\nFinding minimum:")
    min_item = lst.min()
    print("Minimum item:", min_item)

    print("\nFinding index of first occurrence of each element:")
    for item in source:
        ind = lst.index(item)
        print(f"Index of {item}: {ind}")
