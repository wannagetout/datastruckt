from node import Node


class LinkedList:
	def __init__(self, begin=None, end=None):
		self.begin = begin
		self.end = end

	def insert_beginning(self, data):
		new_node = Node(data)
		if self.begin is None:
			self.begin = new_node
		else:
			new_node.next_data = self.begin
			self.begin = new_node
		if self.end is None:
			self.end = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.end is None:
			self.end = new_node
		else:
			self.end.next_data = new_node
			self.end = new_node
		if self.begin is None:
			self.begin = new_node

	def print_ll(self):
		ll_string = ''
		node = self.begin
		if node is None:
			print(None)
		while node:
			ll_string += f' {str(node.data)} ->'
			node = node.next_data

		ll_string += ' None'
		print(ll_string)


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
