from helper import Node, makeLists, strLists, printLists, checkLinks

def flatten_llist(head):
    
    if head == None:
        return None
    
    if (head.prev == None and head.next == None and head.child == None):
        return head
    
    tail_joins = []
    tail_join = None
    cn = head
    
    while cn:
        if cn.child:
            parent = cn
            prev = cn
            tail_joins.append(cn.next)
            cn = cn.child
            parent.child = None
            cn.prev = prev
            prev.next = cn
        elif cn.next == None and len(tail_joins):
            while len(tail_joins):
                tail_join = tail_joins.pop()
                cn.next = tail_join
                if tail_join: 
                    tail_join.prev = cn
                    cn = tail_join
        elif cn:
            cn = cn.next
            
    return head
                

if __name__ == '__main__':
    array = [1, None, 7, None, 8, None, 9, 10]
    head = makeLists(array)
    printLists(head)
    print()
    head = flatten_llist(head)
    printLists(head)
