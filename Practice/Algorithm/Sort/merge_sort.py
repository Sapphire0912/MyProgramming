def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            print("left value: ",left)
            result.append(left.pop(0))
        else:
            print("right value: ",right)
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right
    print("Now_Result : ",result)
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # print("Now_left: ",left)
    # print("Now_right: ",right)

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11]
    print(merge_sort(mylist))

# First in the merge_sort function: 
    # mid = 3
    # left[0:3] -> [20, 9, 100]
    # right[3:] -> [0, 55, 3, 11] 

# First loop(left in merge_sort):
    # left = [20]
    # right = [9, 100]

# First loop(right in merge_sort,because left is a only element in list):
    # left = [9]
    # right = [100]

# Second loop(right in merge_sort):
    # left = [0, 55]
    # right = [3, 11]

# Second loop(left in merge_sort):
    # left = [0]
    # right = [55]

# Third loop(right in merge_sort):
    # left = [3]
    # right = [11]
# return the result to the function of merge(left, right)

# In the merge function:
# First(right):
    # result = [9] + [100]
# First(left):
    # result = [9, 20, 100]

# Second(left):
    # result = [0] + [55]
# Third(right):
    # result = [3] + [11]
# Second(right):
    # left = [0, 55]
    # right = [3, 11]
    # result = [0, 3, 11, 55]

# Now: result [0, 3, 11, 55] and [9, 20, 100]
# Into the function of merge then -->
# return the result is [0, 3, 9, 11, 20, 55, 100] to the answer.
