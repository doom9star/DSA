class MinIndexedPriorityQueue:
    def __init__(self, deg, maxsize):
        self.values = []
        self.child = []
        self.parent = []
        self.pm = []
        self.im = []
        self.sz = 0
        self.N = maxsize
        self.degree = deg

        for index in range(self.N):
            self.values.append(-1)
            self.pm.append(-1)
            self.im.append(-1)
            self.parent.append((index - 1) // self.degree)
            self.child.append(index * self.degree + 1)

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.size() == 0

    def contains(self, ki):
        if 0 <= ki < self.N:
            return self.pm[ki] != -1
        else:
            return False

    def peekMinKeyIndex(self):
        return self.im[0] if self.im[0] != -1 else "Not Found!"

    def pollMinKeyIndex(self):
        minKi = self.peekMinKeyIndex()
        self.delete(minKi)
        return minKi

    def peekMinValue(self):
        return self.values[self.im[0]] if not self.isEmpty() else "Not Found!"

    def pollMinValue(self):
        minVal = self.peekMinValue()
        self.delete(self.peekMinKeyIndex())
        return minVal

    def insert(self, ki, value):
        if not self.contains(ki) and value is not None:
            self.pm[ki] = self.sz
            self.im[self.sz] = ki
            self.values[ki] = value
            self._swim(self.sz)
            self.sz += 1
        else:
            return False

    def valueOf(self, ki):
        return self.values[ki] if 0 <= ki < self.N else "Key Index is Out of bounds!"

    def delete(self, ki):
        if self.contains(ki):
            node_index = self.pm[ki]
            self.sz -= 1
            self._swap(node_index, self.sz)
            self._sink(node_index)
            self._swim(node_index)
            value = self.values[ki]
            del self.values[ki]
            self.pm[ki] = -1
            self.im[self.sz] = -1
            return value
        else:
            return False

    def update(self, ki, value):
        if self.contains(ki) and value is not None:
            node_index = self.pm[ki]
            oldVal = self.values[ki]
            self.values[ki] = value
            self._swim(node_index)
            self._sink(node_index)
            return oldVal
        else:
            return False

    def _sink(self, ni):
        node_index = ni
        minchild = self._minChild(node_index)
        while minchild != -1:
            self._swap(ni, minchild)
            node_index = minchild
            minchild = self._minChild(node_index)

    def _swim(self, ni):
        index = ni
        while self._less(index, self.parent[index]) and self.parent[index] != -1:
            self._swap(index, self.parent[index])
            index = self.parent[index]

    def _swap(self, ki1, ki2):
        self.pm[self.im[ki1]], self.pm[self.im[ki2]] = ki2, ki1
        self.im[ki1], self.im[ki2] = self.im[ki2], self.im[ki1]

    def display(self):
        lst = []
        for index in range(self.sz):
            lst.append(self.im[index])
        return lst

    def _minChild(self, ni):
        index, leftchild, rightchild = -1, min((self.sz, self.child[ni])), min((self.sz, self.child[ni] + self.degree))
        if leftchild < rightchild:
            if self._less(leftchild, ni):
                index = leftchild
            if self._less(rightchild, ni):
                if index != -1:
                    if self._less(rightchild, index):
                        index = rightchild
                else:
                    index = rightchild
        return index

    def _less(self, i, j):
        return self.values[self.im[i]] < self.values[self.im[j]]

    def isMinHeap(self):
        return self._isMinHeap(0)

    def _isMinHeap(self, node):
        start, end = self.child[node], min((self.sz, self.child[node] + self.degree))
        while start < end:
            if not self._less(node, start):
                return False
            if not self._isMinHeap(start):
                return False
            start += 1
        return True


indexedPQ = MinIndexedPriorityQueue(2, 5)

# print(indexedPQ.display())
# print(indexedPQ.values)
# print(indexedPQ.pm)
# print(indexedPQ.im)
# print(indexedPQ.parent)
# print(indexedPQ.child)
# print()
indexedPQ.insert(4, 20)
indexedPQ.insert(0, 87)
indexedPQ.insert(1, 11)
indexedPQ.insert(3, 5)
indexedPQ.insert(2, 15)

# print(indexedPQ.peekMinValue())
# print(indexedPQ.contains(11))
# print(indexedPQ.isEmpty())
# print(indexedPQ.peekMinKeyIndex())
# print(indexedPQ.valueOf(4))
# print(indexedPQ.update(4, 30))
# print(indexedPQ.update(4, 3))
# print(indexedPQ.contains(5))
# print(indexedPQ.isMinHeap())
# print(indexedPQ.delete(4))
# print(indexedPQ.delete(1))
# print(indexedPQ.delete(2))
# # print(indexedPQ.display())
# print(indexedPQ.values)
# print(indexedPQ.pm)
# print(indexedPQ.im)

########################################### PROBLEM #################################################################
# print(indexedPQ.pollMinKeyIndex())
# print(indexedPQ.pollMinKeyIndex())
# print(indexedPQ.pollMinValue())
# print(indexedPQ.pollMinValue())
######################################################################################################################

