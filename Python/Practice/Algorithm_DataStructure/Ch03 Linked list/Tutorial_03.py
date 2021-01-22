# 鏈結串列, 陣列最大差異於: 前者資料散佈於記憶體各處, 後者為記憶體連續空間

# 建立鏈結串列
# 建立節點(節點包含資料和下一筆資料的位置)
class Node(object):
    def __init__(self, data=None):
        self.data = data  # Data
        self.next = None  # Pointer


n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2  # n1 -> n2
n2.next = n3  # n2 -> n3
ptr = n1
while ptr:
    # print(ptr.data)
    ptr = ptr.next  # order: n1 -> n2 -> n3
    pass


# 建立遍歷鏈結串列類別
class LinkedList(object):
    def __init__(self):
        self.head = None  # Linked list first node

    def print_list(self):
        """列印出鏈結串列"""
        ptr2 = self.head  # the indicator points to the first node
        while ptr2:
            print(ptr2.data)
            ptr2 = ptr2.next

    def insert_first(self, newdata):
        """在第一個節點插入新節點"""
        new_node = Node(newdata)  # create new node
        new_node.next = self.head  # new node indicator points to the old first node
        self.head = new_node  # update the first node of the linked list

    def insert_end(self, newdata):
        """在最後的節點插入新節點"""
        new_node = Node(newdata)
        if self.head is None:  # determine whether the linked list is empty
            self.head = new_node
            return
        last_ptr = self.head
        while last_ptr.next:  # move from the first node to the last node
            last_ptr = last_ptr.next
        last_ptr.next = new_node  # the last node indicator points to the new node

    def remove_node(self, rm_val):
        """rm_val: 刪除值"""
        ptr2 = self.head
        prev = 0
        if ptr2:  # if the deleted data is the first node
            if ptr2.data == rm_val:
                self.head = ptr2.next
                return
        while ptr2:
            if ptr2.data == rm_val:
                break
            prev = ptr2
            ptr2 = ptr2.next
        if ptr2 is None:
            return
        prev.next = ptr2.next


link = LinkedList()
link.head = Node(3)
n4 = Node(6)
n5 = Node(9)
link.head.next = n4
n4.next = n5
link.print_list()
print("New Linked List: ")
link.insert_first(12)
link.print_list()
print("New Linked List: ")
link.remove_node(12)
link.print_list()
