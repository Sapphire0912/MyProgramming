# Q1.
class Node(object):
    def __init__(self, data=None):
        self.data = data  # Data
        self.next = None  # Pointer


class LinkedList(object):
    def __init__(self):
        self.head = None  # Linked list first node

    def print_list(self):
        """列印出鏈結串列"""
        ptr2 = self.head  # the indicator points to the first node
        while ptr2:
            print(ptr2.data)
            ptr2 = ptr2.next

    def length(self):
        """計算鏈結串列長度"""
        count = 0
        ptr2 = self.head
        while ptr2:
            if ptr2:
                count += 1
                ptr2 = ptr2.next
            else:
                break
        return count

    def val_times(self):
        """計算目標值出現次數"""
        linked = []
        ptr2 = self.head
        while ptr2:
            if ptr2:
                linked.append(ptr2.data)
                ptr2 = ptr2.next
        print("5: ", linked.count(5), "15: ", linked.count(15), "20: ", linked.count(20))


link = LinkedList()
# link.head = Node(3)
# n4 = Node(6)
# n5 = Node(9)
# n6 = Node(10)
# link.head.next = n4
# n4.next = n5
# n5.next = n6
# link.print_list()
# print("the length of linked list is ", link.length())

# Q2.
# link.head = Node(5)
# n2 = Node(15)
# n3 = Node(5)
# link.head.next = n2
# n2.next = n3
# link.print_list()
# link.val_times()


# Q3.
class DNode(object):
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinked(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_dnode(self, new_node):
        """將節點加入雙向鏈結串列"""
        if isinstance(new_node, DNode):
            if self.head is None:
                self.head = new_node
                new_node.prev = None
                new_node.next = None
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

    def print_front(self):
        ptr = self.head
        while ptr:
            if ptr:
                print(ptr.data)
                ptr = ptr.next

    def print_tail(self):
        ptr = self.tail
        while ptr:
            if ptr:
                print(ptr.data)
                ptr = ptr.prev


d_linked = DoubleLinked()
sun = DNode("Sun")
mon = DNode("Mon")
tue = DNode("Tue")
wed = DNode("Wed")
thu = DNode("Thu")
fri = DNode("Fri")
sat = DNode("Sat")

for i in [sun, mon, tue, wed, thu, fri, sat]:
    d_linked.add_dnode(i)
print("Front: ")
d_linked.print_front()
print("Tail: ")
d_linked.print_tail()
