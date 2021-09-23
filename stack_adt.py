# Stack ADT: Last In First Out

class Stack_List_Imp:
    """This is a simple Stack Abstract Data Type
    implemented by using fixed array"""
    def __init__(self, maxsize: int, items: [int] = []):
        if len(items) > maxsize:
            raise Exception("List is bigger than maxsize")

        self.maxsize: int = maxsize
        self.items: [int] = items.copy()
        self.length: int = len(items)

    # We have two principal operations:
    # 
    # push - add an element to the start
    #
    # pop - remove element from the start
    #
    # Also we will have three additional ones: 
    # top() - return top value without popping it
    # is_empty() - check whether the stack is empty or not
    # is_full() - check whether the stack is full or not

    def push(self, value: int):
        if self.is_full():
            raise Exception("Overflow error. Exceeded the max size!")

        self.items[length] = value
        self.length += 1

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Underflow error. Empty stack")

        self.length -= 1
        return self.items[length]

    def top(self) -> int:
        if self.is_empty():
            raise Exception("Empty stack")

        return self.items[length-1]

    def is_empty(self) -> bool:
        return self.length == 0

    def is_full(self) -> bool:
        return self.length == self.maxsize
