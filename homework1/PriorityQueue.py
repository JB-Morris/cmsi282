class PriorityQueue():
    def __init__(self):
        self.heap = []

    def peek(self):
        return self.heap[0]

    def add(self, item):
        self.heap.append(item)
        self.sift_up(len(self.heap)-1)
        return self

    def remove(self):
        if len(self.heap) == 0:
            raise Exception("Empty Queue")
        if len(self.heap) == 1:
            value = self.heap[0]
            self.heap = []
            return value
        else:
            value = self.heap.pop(0)
            self.sift_down(0)
            return value

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def sift_up(self, index):
        parent_index = (index - 1) / 2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp
            self.sift_up(parent_index)

    def sift_down(self, index):
        child_index = (index * 2) + 1
        if child_index >= len(self.heap):
            return
        if child_index + 1 < len(self.heap) and self.heap[child_index] > self.heap[child_index + 1]:
            child_index += 1
        if self.heap[index] > self.heap[child_index]:
            temp = self.heap[child_index]
            self.heap[child_index] = self.heap[index]
            self.heap[index] = temp
            self.sift_down(child_index)
#
# PQueue = PriorityQueue()
# PQueue.add(20)
# PQueue.add(50)
# PQueue.add(2)
# PQueue.add(27)
# PQueue.add(90)
# PQueue.add(900)
# print PQueue
# print PQueue.remove()
# print PQueue.remove()
# print PQueue.remove()
# print PQueue.remove()
# print PQueue.remove()
# print PQueue.remove()
