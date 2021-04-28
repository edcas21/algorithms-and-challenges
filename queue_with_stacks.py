class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data: any):
        # can only push into stack 1 so that elements stay in the right order
        # Check if there's any elements in stack 2 from previous dequeue or peek operations
        if len(self.stack2):
            # Pop off all elements in stack 2 and push them into stack 1
           for i in range(len(self.stack2)):
               self.stack1.append(self.stack2.pop())
        # Finally just push new data in stack 1
        self.stack1.append(data)
    
    def dequeue(self):
        # to dequeue properly, pop from stack 2
        # check if stack1 has anything
        if len(self.stack1):
            # pop off elements from stack 1 and push them into stack 2
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        # if stack 1 isn't empty then make sure stack 2 has something
        if len(self.stack2):
            # pop off from stack 2
            return self.stack2.pop()
        # Nothing is in either so just return None
        return None
    
    def peek(self):
        # to peek properly, peek from stack 2
        # check if stack1 has anything
        if len(self.stack1):
            # pop off elements from stack 1 and push them into stack 2
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        # if stack 1 isn't empty then make sure stack 2 has something
        if len(self.stack2):
            # peek from stack 2
            return self.stack2[-1]
        # Nothing is in either so just return None
        return None

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

if __name__ == '__main__':
    # queue: [5, 6, 7, 8, 9, 10, 11, 12]
    queue = Queue()
    
    for i in range(1, 11):
        queue.enqueue(i)
    
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    queue.enqueue(11)
    queue.enqueue(12)
    print(queue.stack1)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.stack2)
    print(queue.empty())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.empty())