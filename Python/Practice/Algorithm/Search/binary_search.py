def binary_search(lst, s):
    lst.sort()
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if s > lst[mid]:
            low = mid
        elif s < lst[mid]:
            high = mid
        else:
            return "Element %d is in the %d position of the list" % (s, mid)
    return "Element %d is not in the list." % s

if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11, 47, 33, 10, 88, 49]
    print(binary_search(mylist,55))
# search time: Max: n + log n;  min: 1;  avg: log n