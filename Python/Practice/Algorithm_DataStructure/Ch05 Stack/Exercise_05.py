class MyStack(object):
    def __init__(self):
        self.stack = []
        self.index = 0

    def push(self, data):
        self.stack.append(data)

    def get(self):
        self.index -= 1
        return self.stack[self.index]

    def my_pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack == []

    def cls(self):
        self.stack = []


# Q1.
fruits = list()
fruits.append('Grape')
fruits.append('Mango')
fruits.append('Apple')
stack = MyStack()
for fruit in fruits:
    stack.push(fruit)
    print("Add %s to the stack." % fruit)
print("The stack has %d kind of fruits." % stack.size())

for i in range(0, stack.size()):
    print("remove %s from stack without deleting." % stack.get())

# Q2.
while True:
    stack.cls()
    if stack.is_empty():
        print("end of program.")
        break
    else:
        print(stack.my_pop())
