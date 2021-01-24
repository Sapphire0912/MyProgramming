# 使用 list 模擬堆疊操作
fruits = list()
fruits.append('Grape')
fruits.append('Mango')
fruits.append('Apple')
# print('fruits: ', fruits)
# print('get fruit: ', fruits.pop())
# print('get fruit: ', fruits.pop())
# print('get fruit: ', fruits.pop())


class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def my_pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack == []


stack = MyStack()
for fruit in fruits:
    stack.push(fruit)
    print("Add %s to the stack." % fruit)

print("The stack has %d kind of fruits." % stack.size())
while not stack.is_empty():
    print(stack.my_pop())

# Python 在執行函數呼叫時是以堆疊運作
# 遞迴也屬於堆疊的一種
