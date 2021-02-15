class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        """For queues, the end of the list is saved for popping. A new item is therefore inserted at the
        front of the list: index 0

        The runtime is o(n) because inserting into the 0th index of a list forces all the other items in the list to
        move one index to the right
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Returns and removes the fronmost item in the queue, which is the last item in the list
        Happens in constant time since pop happens in constant time (indexing happens in constant time)
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns the last item in the list: the firt item in the queue"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


if __name__ == "__main__":
    q = Queue()
    q.enqueue('banana')
    print(q)
    q.enqueue('apple')
    print(q)
