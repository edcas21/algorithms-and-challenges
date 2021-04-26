class Stack:

    def __init__(self, array=[]):
        self.array = array
        self.len = len(array)

    def length(self):
        self.len = len(self.array)
        return self.len

    def pop(self):
        if self.length():
            return self.array.pop()
        return None

    def push(self, data):
        self.array.append(data)

    def peek(self):
        if self.length():
            return self.array[-1]
        return None

    def print_stack(self):
        print(self.array)


if __name__ == '__main__':

    stack = Stack()

    for i in range(1, 11):
        stack.push(i)

    stack.print_stack()

    for i in range(5):
        print(stack.pop())
        print('length:', stack.length())

    stack.print_stack()

    for i in range(6):
        print(stack.peek())
        stack.pop()
        print('length:', stack.length())

    stack.print_stack()
