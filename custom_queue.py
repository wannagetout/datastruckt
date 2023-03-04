from typing import Any

from node import Node


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


