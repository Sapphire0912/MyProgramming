from queue import Queue


class MyQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """data 插入佇列"""
        self.queue.insert(0, data)
        print("insert {} into the queue successfully.".format(data))

    def dequeue(self):
        """取出佇列"""
        if len(self.queue):
            return self.queue.pop()
        return None

    def size(self):
        return len(self.queue)


# Q1.
q = MyQueue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print("the length of queue is ", q.size())
for i in range(0, q.size()):
    print("Queue content: ", q.dequeue())

# Q2.
q2 = Queue()
for i in ['漢堡', '薯條', '可樂']:
    q2.put(i)
    print("insert {} into the queue successfully.".format(i))

print("Queue Output: ")
while not q2.empty():
    print(q2.get())
