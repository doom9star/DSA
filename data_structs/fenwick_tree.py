import math as m


class FenwickTree:
    def __init__(self, values):
        self.n = len(values)
        self.tree = None
        self._constructTree(values)

    def _constructTree(self, values):
        values.insert(0, "0L")
        self.tree = values.copy()
        for index in range(1, self.n + 1):
            parent = index + self._lsb(index)
            if parent < self.n:
                self.tree[parent] += self.tree[index]

    def _lsb(self, index):
        binary = "".join(bin(index)[2:])
        pos = []
        for idx in range(len(binary)):
            if binary[idx] == "1":
                pos.append(len(binary) - idx)
        return int(m.pow(2, pos[-1] - 1))

    def prefixSumOfInt(self, index):
        addition = 0
        while index > 0:
            addition += self.tree[index]
            index -= self._lsb(index)
        return addition

    def prefixSumsOfInterval(self, index1, index2):
        if index2 < index1:
            print("Illegal Interval")
        else:
            return self.prefixSumOfInt(index2) - self.prefixSumOfInt(index1 - 1)

    def set(self, index, value):
        return self.update(index, value - self.prefixSumsOfInterval(index, index))

    def get(self, index):
        return self.prefixSumsOfInterval(index, index)

    def update(self, index, value):
        while index < self.n:
            self.tree[index] += value
            index += self._lsb(index)
        return True


values = [10, 25, 5, 8, 55, 89, 44, 90, 78, 45, 34, 22]
tree = FenwickTree(values)
print(tree.tree)
print(tree.prefixSumOfInt(2))
print(tree.update(2, 5))
print(tree.get(10))
print(tree.set(2, 20))
print(tree.tree)
print(tree.prefixSumOfInt(2))
