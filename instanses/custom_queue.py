from typing import Any

from instanses.node import Node


class Queue:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def enqueue(self, data: Any):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next_data = node
			self.tail = node

	def dequeue(self):
		d_node = self.head
		if self.head is None:
			return None
		else:
			self.head = self.head.next_data
			return d_node.data

