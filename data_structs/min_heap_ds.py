class MinHeap:
    def __init__(self, array):
        self._nodes = 0
        self.heap = [0]
        for i in range(len(array)):
            self.heap.append(array[i])
            self.__shiftUp(len(self.heap) - 1)
            self._nodes += 1

    def add(self, value):
        self.heap.append(value)
        self.__shiftUp(len(self.heap) - 1)
        self._nodes += 1

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            self.heap.pop()
            self.__shiftDown(1)
        elif len(self.heap) == 2:
            self.heap.pop()
        else:
            print("MinHeap is Empty!")

    def peek(self):
        print(self.heap[1]) if len(self.heap) > 1 else print("MinHeap is Empty!")

    def display(self):
        print(self.heap[1:])

    def length(self):
        print(self._nodes - 1)

    def __shiftUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__shiftUp(parent)

    def __shiftDown(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        min = index
        if len(self.heap) > leftChild and self.heap[leftChild] < self.heap[min]:
            min = leftChild
        if len(self.heap) > rightChild and self.heap[rightChild] < self.heap[min]:
            min = rightChild
        if min != index:
            self.__swap(min, index)
            self.__shiftDown(min)

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


My_minheap = MinHeap([12, 45, 6, 7, 89, 45, 34, 11, 100, 250, 444])
My_minheap.display()
My_minheap.peek()
My_minheap.pop()
My_minheap.display()
My_minheap.length()
My_minheap.add(2)
My_minheap.display()
