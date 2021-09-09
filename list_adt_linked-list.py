# Linked list implementation by using python code
# NOTE to myself: there is kinda no pointer in Python,
# so I just make some assumptions

class Node:
    """
    This is a simple single Node of a linked list.
    If self.next is False, then it is the end node of the Linked List.
    """
    def __init__(self, value: int = 0, next: "Node" = None):
        self.value = value
        self.next = next


class LinkedList:
    """This is a Link List itself. It only contains a head node"""
    def __init__(self, head: Node):
        self.head = head
        
    # We have to do at least four basic operations with Linked List:
    #
    # 1. Get the nth element of the list
    #
    # 2. Search for a value in the list
    #
    # 3. Insert an element at the front
    #
    # 4. Remove an element by value

    # Get the nth element of the list
    def getItem(self, n: int) -> int:
        count: int = 0
        current: Node = self.head

        while current:
            if count == n:
                return current.value
            current = current.next
            count += 1
        raise IndexError("list index out of range")

    # Search for a value in the list
    def search(self, value: int) -> bool:
        current: Node = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False



if __name__ == '__main__':
    # A test linked list and its nodes
    node_3 = Node(100)
    node_2 = Node(23, node_3)
    node_1 = Node(432, node_2)

    linked_list = LinkedList(node_1)


    print(linked_list.getItem(0))
    print(linked_list.search(432))
    print(linked_list.search(0))