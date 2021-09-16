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

    def __str__(self):
        return f'{{value: {self.value}; next: {self.next}}}'


class LinkedList:
    """This is a Link List itself. It only contains a head node"""
    def __init__(self, head: Node):
        self.head = head

    def __str__(self):
        return f'[{self.head}]'
        
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

    # Insert an element at the front
    def insert_front(self, value: int):
        newHead = Node(value, self.head)
        self.head = newHead

    # Remove an element by value
    def remove(self, value: int):
        # If there are multiple Nodes with the same value,
        # remove the first occurence
        current: Node = self.head
        if current.value == value:
            self.head = current.next
            del current
            return

        while current:
            if current.value == value:
                break
            previous = current
            current = current.next
        if current is not None:
            previous.next = current.next
            del current




if __name__ == '__main__':
    # A test linked list and its nodes
    node_4 = Node(999)
    node_3 = Node(100, node_4)
    node_2 = Node(23, node_3)
    node_1 = Node(432, node_2)

    linked_list = LinkedList(node_1)

    print(linked_list.getItem(3))
    print(linked_list.search(432))
    print(linked_list.search(0))

    print(linked_list)
    linked_list.remove(100)
    print(node_4)
    print(linked_list)
    linked_list.remove(432)
    print(linked_list)
