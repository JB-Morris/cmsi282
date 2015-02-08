__author__ = 'Joseph'

class PriorityQueue:
    def __init__(self):
        self.heap = []
    def peek(self):
        return self.heap[0]
    def add(self, item):
        self.append(item)
        self.sift_up(len(self.heap)-1)
        return self
    def remove(self):
        pass
    def is_empty(self):
        pass
    def __str__(self):
        pass

# k is the parent of node 2k+1 and 2k+2