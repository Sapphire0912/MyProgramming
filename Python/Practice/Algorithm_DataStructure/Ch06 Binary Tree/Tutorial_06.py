# 使用 陣列 建立二元樹
def create_btree(tree, data):
    """使用 array 建立二元樹"""
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

    def search(self, val):
        """搜索特定值"""
        if val < self.data:  # determine whether the val is smaller then root node
            if not self.left:  # if left node is None
                return str(val) + "doesn't exist."
            return self.left.search(val)  # recursive call
        elif val > self.data:
            if not self.right:
                return str(val) + "doesn't exist."
            return self.right.search(val)
        else:  # the val is equal node
            return str(val) + "was found."

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
data = [10, 21, 5, 9, 13, 28, 3, 4, 1, 17, 32]
# for d in data:
#     trees.insert(d)
# print("Inorder: ")
# trees.inorder()
# print("\nPreorder: ")
# trees.preorder()
# print("\nPostorder: ")
# trees.postorder()
# print()
# print(trees.search(13))
# print(trees.search(15))

# user input
# n = eval(input("enter the data you want to search: "))
# print(trees.search(n))


# 二元樹的刪除
class DeleteNode(object):
    def delete_node(self, root, key):
        if root is None:  # determine if the tree exists
            return None
        if key < root.data:  # determine whether the key is smaller then root.data
            root.left = self.delete_node(root.left, key)  # recursive call
            return root
        if key > root.data:
            root.right = self.delete_node(root.right, key)
            return root
        if root.left is None:
            new_root = root.right
            return new_root
        if root.right is None:
            new_root = root.left
            return new_root
        succ = self.max_node(root.left)
        tmp = Node(succ.data)
        tmp.left = self.left_node(root.left)
        tmp.right = root.right
        return tmp

    def left_node(self, node):
        """找出原刪除節點的左子樹"""
        if node.right is None:
            new_root = node.left
            return new_root
        node.right = self.left_node(node.right)
        return node

    def max_node(self, node):
        """找出最大值節點"""
        while node.right:
            node = node.right
        return node


tree = Node()
for d in data:
    tree.insert(d)
tree.inorder()
print()
del_data = 5
print("after delete the data of %d" % del_data)
delete_obj = DeleteNode()
result = delete_obj.delete_node(tree, del_data)
result.inorder()
