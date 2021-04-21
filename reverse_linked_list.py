class Node:
	def __init__(self, value: int, next: 'Node'):
		self.value = value
		self.next = next
		
def llist_to_array(head):
	cur_node = head
	node_array = []
	while cur_node:
		node_array.append(cur_node)
		cur_node = cur_node.next
	return node_array

def reverse_llist(head: Node):
	node_array = llist_to_array(head)
	# node_array[0].next = None
	head = node_array[-1]
	cur_node = head
	for i in range(len(node_array) - 2, -1, -1):
		cur_node.next = node_array[i]
		cur_node = node_array[i]
		if i == 0:
			node_array[i].next = None
	return head

def opt_reverse_llist(head: Node):
	next, cn, prev = None, head, None
	while cn:
		next = cn.next
		cn.next = prev
		prev = cn
		cn = next
	return prev

def rec_reverse_llist(head: Node, prev, cn: Node, next):
	if cn:
		next, cn.next = cn.next, prev
		prev, cn = cn, next
		return rec_reverse_llist(next, prev, cn, next)
	return prev
		
def print_llist(head: Node):
	cur_node = head
	while cur_node:
		print(cur_node.value)
		cur_node = cur_node.next

if __name__ == '__main__':
	node5 = Node(6, None)
	node4 = Node(5, node5)
	node3 = Node(4, node4)
	node2 = Node(3, node3)
	node1 = Node(2, node2)
	head = Node(1, node1)
	print([node.value for node in llist_to_array(head)])
	head = opt_reverse_llist(head)
	print([node.value for node in llist_to_array(head)])
