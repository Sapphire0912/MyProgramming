# 使用 陣列 建立二元樹
def create_btree(tree, data):
    """使用 data 建立二元樹"""
    for i in range(len(data)):
        level = 0
        if i == 0:
            tree[level] = data[i]  # store root node data
        else:
            # find the index that stores the child node data
            while tree[level]:
                if data[i] > tree[level]:
                    level = 2 * (level + 1)
                else:
                    level = 2 * level + 1
        tree[level] = data[i]
        print(i, tree)


btree = [0] * 8
datasets = [10, 21, 5, 9, 13, 28]
# create_btree(btree, datasets)
# for j in range(len(btree)):
#     print("Binary Tree array[%d]: %d " % (j, btree[j]))


# 使用 鏈結串列 建立二元樹
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """建立二元樹"""
        if self.data:  # determine whether there is a root node
            if data < self.data:  # determine whether the value is smaller than root node
                if self.left:
                    self.left.insert(data)  # recursive call
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data  # create root node

    def inorder(self):
        """中序走訪: LDR"""
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        """前序走訪: DLR"""
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        """後序走訪: LRD"""
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")


trees = Node()
data = [10, 21, 5, 9, 13, 28]
for d in data:
    trees.insert(d)
print("Inorder: ")
trees.inorder()
print("\nPreorder: ")
trees.preorder()
print("\nPostorder: ")
trees.postorder()
