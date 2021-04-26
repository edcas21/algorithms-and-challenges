class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def cycle_detector(head: Node):
    t, h = head, head
    p, q = head, None
    while h:
        t, h = t.next, h.next
        if h and h.next:
            h = h.next
            if t.val == h.val:
                q, h = t, None
    while p and q:
        p, q = p.next, q.next
        if p.val == q.val:
            return p.val
    return False


if __name__ == '__main__':
    node9 = Node(9)
    node8 = Node(8, node9)
    node7 = Node(7, node8)
    node6 = Node(6, node7)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    head = Node(1, node2)
    # head = Node()
    # node8.next = node3
    node9.next = node3

    res = cycle_detector(head)

    if res == False:
        print('linked list has no cycle!')
    else:
        print('linked list has a cycle starting at node with value of ', res)
