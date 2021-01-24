# python Queue 模組
from queue import Queue


class MyQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """data 插入佇列"""
        self.queue.insert(0, data)

    def dequeue(self):
        """取出佇列"""
        if len(self.queue):
            return self.queue.pop()
        return None

    def size(self):
        return len(self.queue)


q = MyQueue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
# print("the length of queue is ", q.size())
# for i in range(0, q.size()):
#     print("Queue content: ", q.dequeue())

# 上面的 code 等同於下面的效果
q2 = Queue()
q2.put("Grape")
q2.put("Mango")
q2.put("Apple")
while not q2.empty():
    print(q2.get())
