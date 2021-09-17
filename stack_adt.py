# Stack ADT: Last In First Out

class Stack_List_Imp(object):
    """This is a simple Stack Abstract Data Type
    implemented by using fixed array"""
    def __init__(self, max_size: int, items: [int] = []):
        if len(items) > max_size:
            raise Exception("List is bigger than max size")

        self.max_size: int = max_size
        self.items: [int] = items

    # We have two principal operations:
    # 
    # push - add an element to the start
    #
    # pop - remove element from the start