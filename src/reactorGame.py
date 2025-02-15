import random
import time
import os
DICTIONARY = {1: (0, 0), 2: (0, 1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9:(2,2)}

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
        self._grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.queue = Queue()

    def get_grid(self)->list:
        """
        Returns:
            grid 
        """
        return self._grid
    
    def get_queue(self, amount)->list:
        """
        creates a queue for which numbers will light up in which order
        Returns:
            queue 
        """
        for i in range(amount):
            self.queue.enqueue(random.randint(1, 9))
        return self.queue._items


if __name__ == "__main__":
    keepPlaying = True
    for amount in range(6):
        reactor = Reactor()
        queue_items = reactor.get_queue(amount)
        grid = reactor.get_grid()
        os.system('cls')
        for q in queue_items:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == q:
                        print("  ", end="")
                    else:
                        print(grid[i][j], end=" ")
                print()
            time.sleep(1)
            os.system('cls')
        list = []
        print('Enter the numbers that were shown in order, one by one')
        for i in range(len(queue_items)):
            temp = int(input(""))
            list.append(temp)
        print(queue_items)
        print(list)
        if queue_items == list:
            print('you did it!!!')
        else:
            print('you dumb bitch')


