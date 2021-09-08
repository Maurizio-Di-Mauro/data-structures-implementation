# Linked list implementation by using python code
# NOTE to myself: there is kinda no pointer in Python,
# so I just make some assumptions

class Node:
    """
    This is a simple single Node of a linked list.
    If self.next is False, then it is the end of the Linked List.
    """
    def __init__(self, value: int = 0, next: Node = None):
        self.value = value
        self.next = next

    # We should be able to do at least these four basic operations:
    #
    # 1. Get the nth element of the list
    #
    # 2. Search for a value in the list
    #
    # 3. Insert an element at the front
    #
    # 4. Remove an element by value

    
