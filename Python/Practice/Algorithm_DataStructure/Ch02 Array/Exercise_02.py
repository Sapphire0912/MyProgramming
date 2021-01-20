from array import *
import sys
# format: name = array(datatype, data)

# Q1.
x = array('f', [1.0, 2.0, 5.0, 6.5, 7.0])
for data in x:
    # print(data)
    pass

# Q2.
n = int(input("Enter the index you want to delete: "))
datasets = array('i', [1, 11, 22, 33, 44, 55])
if n >= len(datasets):
    print("index out of list range")
    sys.exit()
else:
    datasets.pop(n)

for data in datasets:
    print(data)
    pass

# Q3.
n = int(input("Enter the index you want to insert: "))
v = int(input("Enter the number: "))

datasets = array('i', [1, 11, 22, 33, 44, 55])
if n >= len(datasets):
    print("index out of list range")
    sys.exit()
else:
    datasets.insert(n, v)

for data in datasets:
    print(data)
    pass
