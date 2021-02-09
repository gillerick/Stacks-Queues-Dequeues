class Stack:
    """Stacks abstract lists. Therefore, behind a stack is a python list object"""

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list
            The runtime is O(1) because appending to the end of a list happens in constant time
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item from the list,
        which is also the top item of the stack

        Runtime is constant time
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    """See the last item that is going to be removed"""

    def peek(self):
        """Shows us the item that is on top of the stack
        Runs in O(1)"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list that is representing the Stack
        Runs in constant time"""
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whether or not the stack is empty
        Testing for equality happens in constant time
        """
        return self.items == []


string = "{[()]}"
symbols = {"{": "}", "[": "]", "(": ")"}
openers = symbols.keys()
s = Stack()


def balance_check(string):
    if len(string) % 2 != 0:
        return False
    if len(string) == 0:
        return True
    index = 0
    while index < len(string):
        symbol = symbols[index]

        if symbol in openers:
            s.push(symbol)
        else:
            if s.is_empty():
                return False

            else:
                top_item = s.pop()
                if symbol != symbols[top_item]:
                    return False
        index += 1
    if s.is_empty():
        return True
    return False


