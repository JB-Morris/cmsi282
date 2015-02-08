# class Queue:

# start old queue

	# def __init__(self):
	# 	self.items = []

	# def peek(self):
	# 	return self.items[0]
	# def add(self, item):
	# 	self.items.append(item)
	# def remove(self):
	# 	self.items.pop
	# def size(self):
	# 	return len(items)
	# def is_empty(self):
	# 	# return not items
	# 	return len(items) == 0
	# def __str__(self):
	# 	return str(self.items)

#end old queue

class Queue:
	class Node:
		def __init__(self, item):
			self.item = item
			self.next = None

	def __init__(self):	
		self.size = 0
		self.head = None
		self.tail = None

	def peek(self):
		if self.is_empty():
			raise ValueError, "The queue is empty."
		return self.head.item
	def add(self, item):
		if self.is_empty():
			self.head = Node(item)
			self.tail = self.head
		else:	
			self.tail.next = Node(item)
			self.tail = self.tail.next
		self.size += 1
		
	def remove(self):
		else:
			item = self.peek()	
			self.head = self.head.next
			self.size -= 1
		if self.is_empty():
			self.tail = None
		return item	
	def is_empty(self):
		return self.size == 0
	def __str__(self):
		result = "["
		node = self.head
		while Node is not None:
			result += node.item + ','
			node = node.next
		result += "]"
		return result