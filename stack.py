from node import Node


class Stack:

	def __init__(self):
		self.head = None

	def push(self, value):
		next_node = self.head
		new_head = Node(value, next_node)
		self.head = new_head
