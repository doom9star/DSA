class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            print("Stack is Empty! - []")
        else:
            del self.stack[len(self.stack) - 1]

    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[0])
        else:
            print("Stack is Empty! - []")

    def size(self):
        print(len(self.stack))

    def isEmpty(self):
        if len(self.stack) > 0:
            print(False)
        else:
            print(True)

    def display(self):
        print(self.stack)


My_stack = Stack()
My_stack.isEmpty()
My_stack.size()
My_stack.push(20)
My_stack.push(54)
My_stack.push(765)
My_stack.push(78)
My_stack.pop()
My_stack.display()
My_stack.isEmpty()
