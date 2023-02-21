from node import Node
from stack import Stack

if __name__ == '__main__':
	a1 = Node(1, None)
	a2 = Node(81, a1)

	print(a1.data)
	print(a2.data)
	print(a1)
	print(a2.next_data)

	stack = Stack()

	stack.push('data1')
	stack.push('data2')
	stack.push('data3')

	print('1')
	print(stack.head.data)
	print('2')
	print(stack.head.next_data.data)
	print('3')
	print(stack.head.next_data.next_data.data)
	print('4')
	print(stack.head.next_data.next_data.next_data)
	print('5')
	print(stack.head.next_data.next_data.next_data.data)

