class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.height = 0
        self.bal_factor = None


class BalancedBinarySearchTree:
    def __init__(self, rootval):
        self.nodes = 0
        self.root = Node(rootval)

    def size(self):
        return self.nodes

    def insert(self, value):
        if not self.contains(value):
            self._insert(self.root, value)
            self.nodes += 1
            return True
        return False

    def _insert(self, root, value):
        if value < root.value:
            if root.leftChild is None:
                root.leftChild = Node(value)
            else:
                return self._insert(root.leftChild, value)
        else:
            if root.rightChild is None:
                root.rightChild = Node(value)
            else:
                return self._insert(root.rightChild, value)
        self.update(root)
        self.balance(root)

    def peekRoot(self):
        return self.root if self.root is not None else "Tree is Empty!"

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, root, value):
        if root is None:
            return False
        elif root.value == value:
            return True
        else:
            if value < root.value:
                return self._contains(root.leftChild, value)
            else:
                return self._contains(root.rightChild, value)

    def update(self, root):
        leftheight = root.leftChild.height if root.leftChild is not None else -1
        rightheight = root.rightChild.height if root.rightChild is not None else -1

        root.height = 1 + max(leftheight, rightheight)
        root.bal_factor = rightheight - leftheight

    def balance(self, root):
        if root.bal_factor == -2:
            if root.leftChild.bal_factor <= 0:
                self._leftLeftCase(root)
            else:
                self._leftRightCase(root)
        elif root.bal_factor == 2:
            if root.rightChild.bal_factor >= 0:
                self._rightRightCase(root)
            else:
                self._rightLeftCase(root)

    def _leftLeftCase(self, node):
        return self._rightRotation(node)

    def _leftRightCase(self, node):
        self._leftRotation(node.leftChild)
        return self._rightRightCase(node)

    def _rightRightCase(self, node):
        return self._leftRotation(node)

    def _rightLeftCase(self, node):
        self._rightRotation(node.rightChild)
        return self._leftLeftCase(node)

    def _rightRotation(self, node):
        newParent = node.leftChild
        node.leftChild = newParent.rightChild
        newParent.rightChild = node
        self.update(node)
        self.update(newParent)
        return newParent

    def _leftRotation(self, node):
        newParent = node.rightChild
        newParent.leftChild = node
        node.rightChild = newParent.leftChild
        self.update(node)
        self.update(newParent)
        return newParent

    def remove(self, value):
        if self.contains(value):
            self._remove(self.root, value)
            self.nodes -= 1
            return True
        return False

    def _remove(self, root, value):
        if root is None:
            return None
        if value < root.value:
            root.leftChild = self._remove(root.leftChild, value)
        elif value > root.value:
            root.rightChild = self._remove(root.rightChild, value)
        else:
            if root.leftChild is None:
                return root.rightChild
            elif root.rightChild is None:
                return root.leftChild
            else:
                if root.leftChild.height > root.rightChild.height:
                    successorValue = self._findMax(root.leftChild)
                    root.value = successorValue
                    root.leftChild = self._remove(root.leftChild, successorValue)

                else:
                    successorValue = self._findMin(root.rightChild)
                    root.value = successorValue
                    root.rightChild = self._remove(root.rightChild, successorValue)
        self.update(root)
        self.balance(root)

    def _findMax(self, node):
        curnode = node
        while curnode.rightChild is not None:
            curnode = curnode.rightChild
        return curnode.value

    def _findMin(self, node):
        curnode = node
        while curnode.leftChild is not None:
            curnode = curnode.leftChild
        return curnode.value

    def printAsList(self):
        queue = [self.root]
        while len(queue) > 0:
            parent = queue[0]
            if parent.leftChild is not None:
                queue.append(parent.leftChild)
            if parent.rightChild is not None:
                queue.append(parent.rightChild)
            print(parent.value, end=" ")
            queue.remove(parent)

    def height(self):
        return self.root.height


tree = BalancedBinarySearchTree(20)
print(tree.size())
print(tree.insert(20))
print(tree.insert(15))
print(tree.insert(25))
print(tree.insert(30))
print(tree.insert(45))
print(tree.insert(10))
print(tree.insert(5))
print(tree.size())
tree.printAsList()
