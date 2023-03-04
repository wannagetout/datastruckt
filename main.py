from stack import Stack
from custom_queue import Queue


if __name__ == '__main__':

	queue = Queue()
	queue.enqueue('data1')
	queue.enqueue('data2')
	queue.enqueue('data3')

	print(queue.head.data)
	print(queue.head.next_data.data)
	print(queue.tail.data)
	print(queue.tail.next_data)
	print(queue.tail.next_data.data)
