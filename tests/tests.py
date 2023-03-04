import unittest

import node
from stack import Stack
from node import Node
from custom_queue import Queue


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
