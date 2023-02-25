import unittest

import node
from stack import Stack
from node import Node


class TestNode(unittest.TestCase):

	def test_Stack(self):
		stack = Stack()
		stack.push('data1')
		stack.push('data2')
		self.assertEqual(stack.head.data, 'data2')
		self.assertEqual(stack.pop(), 'data2')
