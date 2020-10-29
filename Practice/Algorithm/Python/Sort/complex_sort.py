class Sort:
    s = 5
    def bubble(self,lst):
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if lst[i] < lst[j]:  # small to large; lst[i] > lst[j]: large to small
                    lst[i], lst[j] = lst[j], lst[i]
        return lst 

    def insertion(self,lst):
        for i in range(1,len(lst)):
            tmp = lst[i]
            j = i - 1
            while j >= 0 and tmp < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = tmp
        return lst
                
    def bucket(self,lst):
        can = []
        for i in range(max(lst)+1):
            can.append(0)
        for data in lst:
            can[data] = can[data] + 1
        
        index = 0
        for i in range(len(can)):
            if can[i] != 0:
                for j in range(can[i]):
                    lst[index] = i
                    index += 1
        return lst

    def merge(self,lst):
        def pos(left,right):
            result = []
            while left and right:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))

            if left:
                result += left
            if right:
                result += right
            return result

        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        left = Sort.merge(self,left)
        right = Sort.merge(self,right)
        return pos(left, right)

    def heap(self,lst):
        def sift(start,end):
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and lst[child] < lst[child+1]:
                    child += 1
                if lst[root] < lst[child]:
                    lst[root], lst[child] = lst[child], lst[root]
                    root = child
                else:
                    break

        for start in range(len(lst) // 2, -1, -1):
            sift(start, len(lst) - 1)

        for end in range(len(lst) - 1, 0, -1):
            lst[0], lst[end] = lst[end], lst[0]
            sift(0, end - 1)
        return lst

    def quick(self,lst):
        left = []
        right = []
        key = []

        if len(lst) <= 1:
            return lst
        else:
            first = lst[0]
            for i in lst:
                if i < first:
                    left.append(i)
                elif i > first:
                    right.append(i)
                else:
                    key.append(i)
        
        left = Sort.quick(self,left)
        right = Sort.quick(self,right)
        return left + key + right