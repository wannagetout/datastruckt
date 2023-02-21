import unittest

import node
from stack import Stack
from node import Node


class TestNode(unittest.TestCase):

	def test_node_structure(self):
		node1 = Node(1, None)
		node2 = Node(90, node1)
		stack = Stack()
		stack.push('data1')
		stack.push('data2')
		stack.push('data3')
		self.assertEqual(node1.data, 1)
		self.assertEqual(node2.data, 90)
		self.assertEqual(type(node1), node.Node)
		self.assertEqual(type(node2), node.Node)
		self.assertEqual(stack.head.data, 'data3')
		self.assertEqual(stack.head.next_data.data, 'data2')
		self.assertEqual(stack.head.next_data.next_data.data, 'data1')
		self.assertEqual(stack.head.next_data.next_data.next_data, None)
