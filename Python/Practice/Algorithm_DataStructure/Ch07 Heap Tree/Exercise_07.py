import heapq
# Q1.
# h = list()
# for d in [10, 21, 5, 9, 13, 28, 3]:
#     heapq.heappush(h, d)
#     print("Heap tree after inserting", d, ": h =", h)

# Q2.


class Heaptree(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def data_down(self, depth):
        while (2 * depth + 2) <= self.size:
            min_depth = self.get_min_depth(depth)
            if self.heap[depth] > self.heap[min_depth]:
                self.heap[depth], self.heap[min_depth] = self.heap[min_depth], self.heap[depth]
            depth = min_depth

    def data_up(self, depth):
        while ((depth - 1) // 2) >= 0:
            if self.heap[depth] < self.heap[(depth-1)//2]:
                self.heap[depth], self.heap[(depth-1)//2] = self.heap[(depth-1)//2], self.heap[depth]
            depth = (depth - 1) // 2

    def get_min_depth(self, depth):
        if 2 * depth + 2 >= self.size:
            return 2 * depth + 1
        else:
            if self.heap[2*depth+1] < self.heap[2*depth+2]:
                return 2 * depth + 1
            else:
                return 2 * depth + 2

    def build_heap(self, my_list: list):
        depth = (len(my_list) // 2) - 1
        self.size = len(my_list)
        self.heap = my_list
        while depth >= 0:
            self.data_down(depth)
            depth -= 1

    def my_pop(self):
        pop_data = self.heap[0]  # get the data of first index
        self.size -= 1  # get last index
        self.heap[0] = self.heap[self.size]  # last data move to first index
        self.heap.pop()  # delete last index
        self.data_down(0)  # rearrange heap tree
        return pop_data

    def my_push(self, data):
        self.heap.append(data)
        self.size += 1
        self.data_up(self.size - 1)


ht = Heaptree()
h = [10, 21, 5, 9, 13, 28, 3]
print("Before: ", h)
ht.build_heap(h)
print("After: ", h)
# val = ht.my_pop()
# print("the maximum element as", val)
# print("After deletion: ", h)

# Q3.
for d in [2, 1, 6]:
    ht.my_push(d)
    print("Heap tree after inserting", d, "as", h)
