# 使用 Python 內建模組 heapq
import heapq

# 建立二元堆積樹
# 使用 heapify(data) 建立
# data = [10, 21, 5, 9, 13, 28, 3]
# print("Before: ", data)
# heapq.heapify(data)
# print("After: ", data)

# 放入元素到堆積樹
# heappush(heap, item)
# print("Before insertion: ", data)
# heapq.heappush(data, 11)
# print("1st After insertion: ", data)
# heapq.heappush(data, 2)
# print("2nd After insertion: ", data)

# 從堆積樹取出和刪除元素
# heappop()
# print("Before taking out: ", data)
# val = heapq.heappop(data)
# print("Take out the element as ", val)
# print("After taking out: ", data)

# 傳回最大或最小的 n 個元素
# print("the maximum 3 elements as ", heapq.nlargest(3, data))
# print("the minimum 3 elements as ", heapq.nsmallest(3, data))

# 取出堆積最小值和插入新元素
# x = heapq.heapreplace(data, 7)
# print("Take out the element as ", x)
# print("After taking out: ", data)

# tuple 也可以當成堆積的資料
# ex. heapq.heappush(heap, (any_data))


# 自己建立堆積樹
class Heaptree(object):
    def __init__(self):
        self.heap = []  # heap tree linked list
        self.size = 0  # number of heap tree elements

    def data_down(self, i):
        """如果節點值大於子節點值則資料與較小的子節點值對調"""
        while (2 * i + 2) <= self.size:  # continue if child node exists
            mi = self.get_min_index(i)  # get the child node with the smaller value
            if self.heap[i] > self.heap[mi]:  # determine whether the current node greater than the child node
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]  # swap
            i = mi

    def get_min_index(self, i):
        """傳回較小值的子節點索引
        the index of left node as 2 * i + 1
        the index of right node as 2 * i + 2
        """
        if 2 * i + 2 >= self.size:
            return i * 2 + 1
        else:
            if self.heap[i*2+1] < self.heap[i*2+2]:
                return i * 2 + 1
            else:
                return i * 2 + 2

    def build_heap(self, my_list: list):
        """建立堆積樹"""
        i = (len(my_list) // 2) - 1
        self.size = len(my_list)
        self.heap = my_list
        while i >= 0:
            self.data_down(i)
            print("Current Heap: ", self.heap)
            i -= 1


h = [10, 21, 5, 9, 13, 28, 3]
print("Before execution: ", h)
obj = Heaptree()
obj.build_heap(h)
print("After execution: ", h)
