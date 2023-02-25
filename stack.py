from node import Node


class Stack:

	def __init__(self):
		self.head = None

	def push(self, value):
		next_node = self.head
		new_head = Node(value, next_node)
		self.head = new_head

	def pop(self):
		pop_head = self.head
		pop_data = pop_head.data
		self.head = pop_head.next_data
		return pop_data
