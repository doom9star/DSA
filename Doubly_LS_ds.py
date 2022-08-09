class Node:
    def __init__(self, data):
        self.data = data
        self.prevnode = None
        self.nextnode = None


class DLinkedList:
    def __init__(self):
        self.rootnode = None
        self.tailnode = None
        self.nodes = 0

    def add(self, data):
        curnode = self.rootnode
        newnode = Node(data)
        if curnode is None:
            self.rootnode = newnode
            self.tailnode = newnode
            self.nodes += 1
        else:
            while curnode.nextnode is not None:
                curnode = curnode.nextnode
            curnode.nextnode = newnode
            self.tailnode = newnode
            self.nodes += 1
            newnode.prevnode = curnode

    def delete(self, data):
        curnode = self.rootnode
        prevnode = None
        if curnode is None:
            print("Linked List is empty")
        else:
            if curnode.nextnode is None or curnode.data == data:
                if curnode.data == data and curnode.nextnode is None:
                    self.rootnode = None
                    self.tailnode = None
                    del curnode
                    self.nodes -= 1
                else:
                    self.rootnode = curnode.nextnode
                    del curnode
                    self.nodes -= 1
            else:
                while curnode.nextnode is not None:
                    if curnode.data == data:
                        node = curnode.nextnode
                        prevnode.nextnode = node
                        node.prevnode = prevnode
                        del curnode
                        self.nodes -= 1
                        break
                    else:
                        prevnode = curnode
                        curnode = curnode.nextnode
                        if curnode.data == data and self.tailnode is curnode:
                            self.tailnode = prevnode
                            prevnode.nextnode = None
                            del curnode
                            self.nodes -= 1
                            break

    def isEmpty(self):
        if self.rootnode is None:
            print(True)
        else:
            print(False)

    def size(self):
        print(self.nodes)

    def peek(self):
        print(self.rootnode.data) if self.rootnode is not None else print("Linked list is Empty!")

    def forward_traversal(self):
        if self.rootnode is None:
            print("Linked List is Empty! - []")
        else:
            elements = []
            curnode = self.rootnode
            if curnode.nextnode is None:
                elements.append(curnode.data)
                print(elements)
            else:
                while curnode.nextnode is not None:
                    elements.append(curnode.data)
                    curnode = curnode.nextnode
                    if curnode.nextnode is None:
                        elements.append(curnode.data)
                print(elements)

    def backward_traversal(self):
        if self.tailnode is None:
            print("Linked list is Empty! - []")
        else:
            elements = []
            curnode = self.tailnode
            if curnode.prevnode is None:
                elements.append(curnode.data)
                print(elements)
            else:
                while curnode.prevnode is not None:
                    elements.append(curnode.data)
                    curnode = curnode.prevnode
                    if curnode.prevnode is None:
                        elements.append(curnode.data)
                print(elements)


My_Dlinked_list = DLinkedList()
My_Dlinked_list.add(65)
My_Dlinked_list.add(56)
My_Dlinked_list.add(78)
My_Dlinked_list.add(11)
My_Dlinked_list.add(6)
# # My_Dlinked_list.isEmpty()
My_Dlinked_list.forward_traversal()
# # My_Dlinked_list.size()
# My_Dlinked_list.delete(65)
My_Dlinked_list.delete(11)
My_Dlinked_list.delete(6)
# # My_Dlinked_list.display()
# My_Dlinked_list.size()
My_Dlinked_list.delete(56)
My_Dlinked_list.forward_traversal()
My_Dlinked_list.peek()
My_Dlinked_list.backward_traversal()