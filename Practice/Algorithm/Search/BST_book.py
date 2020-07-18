class BinaryNode:
    def __init__(self, value = None):
        # 建立二元節點
        self.value = value
        self.left = None
        self.right = None

    def add(self, val): # 搭配已知的值 將Node加入BST中 (BST = Binary Search Tree)
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)

class BinaryTree:
    def __init__(self):
        # "建立空的BST"
        self.root = None
    
    def insert(self, value):
        # 將值插入BST的正確位置
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.insert(value)

    def contains(self, target):
        # 檢查BST是否含有目標值
        node = self.root
        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                node = node.right
        return True
