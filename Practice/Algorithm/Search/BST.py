class BinaryTree:
    def __init__(self):
        self.root = None
    
    def __iter__(self):
        # 樹中元素的 中序走訪(in-order traversal)
        if self.root:
            return self.root.inorder()

    def add(self, value):
        # 將值插入二元樹的適當位置
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.root.add(value)

class BinaryNode:
    def __init__(self, value = None):
        # 建立二元節點
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
    
    def inorder(self):
        # 紮根於已知節點的樹 的 中序走訪
        if self.left:
            for n in self.left.inorder():
                yield n

        yield self.value

        if self.right:
            for n in self.right.inorder():
                yield n

    def computeHeight(self):
        # 由子節點計算BST中節點的高度
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)
        self.height = height + 1
    
    def heightDifference(self):
        # 計算BST中節點的子節點高度差異
        leftTarget = 0
        rightTarget = 0
        if self.left:
            leftTarget = 1 + self.left.height
        if self.right:
            rightTarget = 1 + self.right.height
        return leftTarget - rightTarget
    
    def add(self, val):
        # 搭配值與所需的再平衡作業,來將新的節點加入BST
        newRoot = self
        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
            if self.heightDifference() == 2:
                if val <= self.left.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()
            else:
                self.right = self.addToSubTree(self.right, val)
                if self.heightDifference() == -2:
                    if val > self.right.value:
                        newRoot = self.rotateLeft()
                    else:
                        newRoot = self.rotateRightLeft()
        newRoot.computeHeight()
        return newRoot
    
    def addToSubTree(self, parent, val):
        # 將val 加入父的子樹(假如存在的話), 如果因為旋轉作業而有變更, 則傳回其根節點
        if parent is None:
            return BinaryNode(val)
        parent = parent.add(val)
        return parent
    
    def rotateRight(self):
        # 沿著已知的節點執行 向右旋轉
        newRoot = self.left
        grandson = newRoot.right
        self.left = grandson
        newRoot.right = self

        self.computeHeight()
        return newRoot

    def rotateRightLeft(self):
        # 沿著已知的節點執行右旋轉接著左旋
        child = self.right
        newRoot = child.left
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.left = grand2
        self.right = grand1

        newRoot.left = self
        newRoot.right = child

        child.computeHeight()
        self.computeHeight()
        return newRoot
    
    def rorateLeft(self):
        # 沿著已知的節點執行 向左旋轉
        newRoot = self.right
        grandson = newRoot.left
        self.right = grandson
        newRoot.right = self
        
        self.computeHeight()
        return newRoot
    
    def rotateLeftRight(self):
        # 沿著已知節點執行左旋轉接著右旋
        child = self.left
        newRoot = child.right
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.right = grand1
        self.left = grand2
        newRoot.left = child
        newRoot.right = self

        child.computeHeight()
        self.computeHeight()
        return newRoot

    def removeFromParent(self, parent, val):
        # 移除作業的輔助函式. 在移除具有子節點的節點時確保適當的行為
        if parent:
            return parent.remove(val)
        return None
    
    def remove(self, val):
        # 從二元樹移除val. 在二元樹中連同remove方法一起運作
        newRoot = self
        if val == self.value:
            if self.left is None:
                return self.right
            
            child = self.left
            while child.right:
                child = child.right

            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey

            if self.heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rorateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        elif val < self.value:
            self.left = self.removeFromParent(self.left, val)
            if self.heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rorateLeft()
                else:
                    newRoot = self.rotateRightLeft()
        else:
            self.right = self.removeFromParent(self.right, val)
            if self.heightDifference() == 2:
                if self.left.heightDifference() >= 0:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()
        
        newRoot.computeHeight()
        return newRoot

bt = BinaryTree()
for i in range(7, 0, -1):
    bt.add(i)

for v in bt:
    print(v)