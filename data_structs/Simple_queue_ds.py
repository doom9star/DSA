class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) < 1:
            print("Queue is Empty! = []")
        else:
            del self.queue[0]

    def size(self):
        print(len(self.queue))

    def isEmpty(self):
        if len(self.queue) > 0:
            print(False)
        else:
            print(True)

    def display(self):
        print(self.queue)


My_queue = SimpleQueue()
My_queue.isEmpty()
My_queue.enqueue(34)
My_queue.enqueue(14)
My_queue.enqueue(65)
My_queue.enqueue(78)
My_queue.enqueue(11)
My_queue.display()
My_queue.dequeue()
My_queue.size()
My_queue.display()
