class search():
    def linear(self, lst, s):
        for i in range(len(lst)):
            if s == lst[i]:
                ch = "Element %d is in the %d position of the list." % (s, i + 1)
                return ch
        return "Element %d is not in the list." % s

    def binary(self, lst, s):
        lst.sort()
        low, high = 0, len(lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if s > lst[mid]:
                low = mid
            elif s < lst[mid]:
                high = mid
            else:
                return "Element %d is in the %d position of the list." %(s, mid)
        return "Element %d is not in the list." % s