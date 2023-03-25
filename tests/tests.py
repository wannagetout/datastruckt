import unittest

from instanses.stack import Stack
from instanses.custom_queue import Queue
from instanses.linked_list import LinkedList


class TestNode(unittest.TestCase):

	def test_Stack(self):
		stack = Stack()
		stack.push('data1')
		stack.push('data2')
		self.assertEqual(stack.head.data, 'data2')
		self.assertEqual(stack.pop(), 'data2')

	def test_Queue(self):
		queue = Queue()
		queue.enqueue('data1')
		queue.enqueue('data2')
		queue.enqueue('data3')

		self.assertEqual(queue.head.data, 'data1')
		self.assertEqual(queue.head.next_data.data, 'data2')
		self.assertEqual(queue.tail.data, 'data3')
		self.assertEqual(queue.tail.next_data, None)

		self.assertEqual(queue.dequeue(), 'data1')
		self.assertEqual(queue.dequeue(), 'data2')
		self.assertEqual(queue.dequeue(), 'data3')
		self.assertEqual(queue.dequeue(), None)

	def test_LinkedList(self):
		ll = LinkedList()
		ll.insert_beginning({'id': 1})
		ll.insert_at_end({'id': 2})
		ll.insert_at_end({'id': 3})
		ll.insert_beginning({'id': 0})
		self.assertEqual(ll.to_list(), [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}])
		self.assertEqual(ll.get_data_by_id(2), {'id': 2})
