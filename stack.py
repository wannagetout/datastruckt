from node import Node


class Stack:

	def __init__(self):
		self.head = None

	def push(self, value):
		new_node = Node(value)
		new_node.next_data = self.head
		self.head = new_node
