class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.count = 0

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')

    def leaf_count(self, root):
        if not (root.left or root.right):
            return 1
        if root.left:
            self.count += root.left.leaf_count(root.left)
        if root.right:
            self.count += root.right.leaf_count(root.right)
        return self.count

    def depth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.depth(root.left), self.depth(root.right))


class DelNode(object):
    def target(self, root, val):
        if root is None:
            return None

        if val < root.data:
            root.left = self.target(root.left, val)
            return root

        if val > root.data:
            root.right = self.target(root.right, val)
            return root

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        min_right = self.min_node(root.right)
        tmp = Node(min_right.data)
        tmp.right = self.right_node(root.right)
        return tmp

    def min_node(self, root):
        """找出最小值"""
        while root.left:
            root = root.left
        return root

    def right_node(self, root):
        """找出剩下的右節點"""
        pass
        # print("-----")
        # if root.right is None:
        #     return root.left
        # root.right = self.right_node(root.right)
        # return root


tree = Node()
datasets = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datasets:
    tree.insert(d)

# Q1.
# print("Preorder: ")
# tree.preorder()
# print()
# print(tree.leaf_count(tree))

# Q2.
# print("Postorder: ")
# tree.postorder()
# print()
# print(tree.depth(tree))

# Q3. wait
# print("Postorder: ")
# tree.postorder()
# print()
# del_node = DelNode()
# del_node.target(tree, 10)
# print("Postorder: ")
# tree.postorder()
# print()
