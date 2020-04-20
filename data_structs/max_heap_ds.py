class MaxHeap:
    def __init__(self, array):
        self.nodes = 0
        self.heap = [0]
        for i in range(len(array)):
            self.heap.append(array[i])
            self.__shiftUp(len(self.heap) - 1)
            self.nodes += 1

    def add(self, value):
        self.nodes += 1
        self.heap.append(value)
        self.__shiftUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            self.heap.pop()
            self.__shiftDown(1)
        elif len(self.heap) == 2:
            self.heap.pop()
        else:
            print("MaxHeap is Empty")

    def display(self):
        print(self.heap[1:])

    def peek(self):
        print(self.heap[1]) if len(self.heap) >= 1 else print("MaxHeap is Empty!")

    def __shiftUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] >= self.heap[parent]:
            self.__swap(index, parent)
            self.__shiftUp(parent)

    def __shiftDown(self, index):
        leftchild = index * 2
        rightchild = index * 2 + 1
        lar = index
        if len(self.heap) > leftchild and self.heap[leftchild] > self.heap[lar]:
            lar = leftchild
        if len(self.heap) > rightchild and self.heap[rightchild] > self.heap[lar]:
            lar = rightchild
        if lar != index:
            self.__swap(index, lar)
            self.__shiftDown(lar)

    def __swap(self, ele1, ele2):
        self.heap[ele1], self.heap[ele2] = self.heap[ele2], self.heap[ele1]

    def length(self):
        print(self.nodes)


My_maxheap = MaxHeap([10, 5, 6, 54, 78, 34, 21, 89, 54, 44])
My_maxheap.display()
My_maxheap.peek()
My_maxheap.add(102)
My_maxheap.display()
My_maxheap.peek()
My_maxheap.pop()
My_maxheap.display()
My_maxheap.pop()
My_maxheap.display()
