class Queue:
    def __init__(self):
        self._items = []
    def enqueue(self, item):
        self._items.insert(0,item)
    def dequeue(self):
        return self._items.pop()
    def isEmpty(self):
        return self._items == []
    def size(self):
        return len(self._items)
    def clear(self):
        self._items=[]

class Reactor():
    def __init__(self):
        self._items = []
        self.queue = Queue()
    