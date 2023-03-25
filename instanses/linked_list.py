from instanses.node import Node


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

	def to_list(self):
		linked_list_obj = []
		linked_list_data = []
		if self.begin is not None:
			linked_list_obj.append(self.begin)
		else:
			return linked_list_data
		while True:
			if linked_list_obj[len(linked_list_obj) - 1].next_data is None:
				break
			else:
				linked_list_obj.append(linked_list_obj[len(linked_list_obj) - 1].next_data)
		for obj in linked_list_obj:
			linked_list_data.append(obj.data)
		return linked_list_data

	def get_data_by_id(self, id_):
		try:
			linked_list_data = self.to_list()
			for data in linked_list_data:
				if data['id'] == id_:
					return data
		except TypeError:
			print(f'Данные не являются словарем или в словаре нет id {id_}')


# ll = LinkedList()
#
# ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
# ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
# ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
# ll.insert_beginning({'id': 0, 'username': 'serebro'})
#
# # метод to_list()
# lst = ll.to_list()
# for item in lst:
# 	print(item)
#
# # get_data_by_id()
# user_data = ll.get_data_by_id(3)
# print('--')
# print(user_data)

# работа блока try/except
ll = LinkedList()
ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
for o in ll.__dict__.values():
	print(o.__dict__)

user_data = ll.get_data_by_id(2)
print(user_data)
