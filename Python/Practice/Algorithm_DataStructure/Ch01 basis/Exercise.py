import itertools

# Q1.
methods = 1
for i in range(1, 21):
    methods *= i
# print(methods)

# Q2.
t = 0.0000000001
# print(int(methods * t))

# Q3.
elements = ['a', 'b', 'c', 'd', 'e', 'f']
c = itertools.permutations(elements)
count = 0
for i in c:
    count += 1
#     print(i)
# print(count)

# Q4. 同 Q3
