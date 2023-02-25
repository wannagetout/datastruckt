from node import Node
from stack import Stack

if __name__ == '__main__':

	stack = Stack()
	stack.push('data1')
	data = stack.pop()

	print(stack.head)
	print(data)

	stack = Stack()
	stack.push('data1')
	stack.push('data2')
	data = stack.pop()

	print(stack.head.data)
	print(data)
