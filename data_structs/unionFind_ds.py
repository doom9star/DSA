class UnionFind:
    def __init__(self, size):
        self.size = size
        self.numOfComponents = size
        self.id = []
        self.sz = []
        self._construct()

    def _construct(self):
        for index in range(self.size):
            self.id.append(index)
            self.sz.append(1)

    def find(self, index):
        root = index
        while root != self.id[root]:
            root = self.id[root]

        while index != root:
            next = self.id[index]
            self.id[index] = root
            index = next
        return root

    def connected(self, ele1, ele2):
        return self.find(ele1) == self.find(ele2)

    def components(self):
        return self.numOfComponents

    def unify(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)

        if root1 == root2:
            return
        if self.sz[root1] > self.sz[root2]:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        else:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        self.numOfComponents -= 1
        return True


ufo = UnionFind(10)
print(ufo.unify(4, 7))
print(ufo.unify(3, 7))
print(ufo.id)
print(ufo.find(4))
print(ufo.connected(3, 4))
print(ufo.numOfComponents)