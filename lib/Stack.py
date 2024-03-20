class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        if len(items) <= self.limit:
            self.items = items

    def isEmpty(self):
        return [True if self.items else False]

    def push(self, item):
        if len(self.items) < 100:
            self.items.push(item)
        else:
            raise MemoryError("Stack Full")

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        pass

    def full(self):
        pass

    def search(self, target):
        pass
