class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None


class SinLinkedList:
    def __init__(self):
        self.rootnode = None
        self.nodes = 0

    def add(self, data):
        if self.rootnode is None:
            self.rootnode = Node(data)
            self.nodes += 1
        else:
            curnode = self.rootnode
            while curnode.nextnode is not None:
                curnode = curnode.nextnode
            curnode.nextnode = Node(data)
            self.nodes += 1

    def delete(self, data):
        if self.rootnode is None:
            print("Linked List is empty!")
        else:
            curnode = self.rootnode
            prevnode = None
            if curnode.data == data and curnode is self.rootnode and curnode.nextnode is None:
                self.rootnode = None
                del curnode
                self.nodes -= 1
                return
            while curnode.nextnode is not None:
                if curnode.data == data and curnode is self.rootnode:
                    self.rootnode = curnode.nextnode
                    del curnode
                    self.nodes -= 1
                    break
                elif curnode.data == data:
                    prevnode.nextnode = curnode.nextnode
                    del curnode
                    self.nodes -= 1
                    break
                else:
                    prevnode = curnode
                    curnode = curnode.nextnode
                    if curnode.data == data:
                        prevnode.nextnode = curnode.nextnode
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

    def display(self):
        nodes = []
        if self.rootnode is not None:
            curnode = self.rootnode
            if curnode.nextnode is None and curnode is self.rootnode:
                nodes.append(curnode.data)
            while curnode.nextnode is not None:
                nodes.append(curnode.data)
                curnode = curnode.nextnode
                if curnode.nextnode is None:
                    nodes.append(curnode.data)
                    break
            print(nodes)
        else:
            print(nodes)


My_SLinked_list = SinLinkedList()
My_SLinked_list.size()
My_SLinked_list.display()
My_SLinked_list.add(20)
My_SLinked_list.add(45)
My_SLinked_list.add(56)
My_SLinked_list.add(12)
My_SLinked_list.add(82)
My_SLinked_list.display()
My_SLinked_list.isEmpty()
My_SLinked_list.delete(20)
My_SLinked_list.display()
My_SLinked_list.delete(12)
My_SLinked_list.display()
My_SLinked_list.delete(56)
My_SLinked_list.display()
My_SLinked_list.delete(82)
My_SLinked_list.display()
My_SLinked_list.size()
