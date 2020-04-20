class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree:
    def __init__(self):
        self.rootnode = None
        self.nodes = 0

    def add(self, data):
        self.nodes += 1
        self.__add(self.rootnode, data)

    def __add(self, root, data):
        if data <= root.data:
            if root.leftChild is None:
                root.leftChild = Node(data)
            else:
                self.__add(root.leftChild, data)
        else:
            if root.rightChild is None:
                root.rightChild = Node(data)
            else:
                self.__add(root.rightChild, data)

    def addRoot(self, data):
        self.rootnode = Node(data)

    def removeRoot(self):
        pass

    def delete(self, data):
        pass

    def inorder_traveral(self):
        if self.rootnode is not None:
            self.__inorder_traversal(self.rootnode)
        else:
            print("Binary Tree is Empty!")

    def __inorder_traversal(self, root):
        if root is not None:
            self.__inorder_traversal(root.leftChild)
            print(root.data)
            self.__inorder_traversal(root.rightChild)

    def postorder_traversal(self):
        if self.rootnode is not None:
            self.__postorder_traversal(self.rootnode)
        else:
            print("Binary Tree is Empty!")

    def __postorder_traversal(self, root):
        if root is not None:
            self.__postorder_traversal(root.leftChild)
            self.__postorder_traversal(root.rightChild)
            print(root.data)

    def preorder_traversal(self):
        if self.rootnode is not None:
            self.__preorder_traversal(self.rootnode)
        else:
            print("Binary Tree is Empty!")

    def __preorder_traversal(self, root):
        if root is not None:
            print(root.data)
            self.__preorder_traversal(root.leftChild)
            self.__preorder_traversal(root.rightChild)

    def size(self):
        print(self.nodes)

    def isEmpty(self):
        print(True) if self.rootnode is None else print(False)

    def showRoot(self):
        print(self.rootnode.data)


My_Binary_tree = BinaryTree()
My_Binary_tree.size()
My_Binary_tree.addRoot(20)
My_Binary_tree.showRoot()
My_Binary_tree.add(56)
My_Binary_tree.add(11)
My_Binary_tree.add(24)
My_Binary_tree.add(5)
My_Binary_tree.add(10)
My_Binary_tree.add(90)
My_Binary_tree.size()
My_Binary_tree.isEmpty()
My_Binary_tree.inorder_traveral()
