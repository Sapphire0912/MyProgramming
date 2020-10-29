def quick_sort(lst):
    key_value = []
    left_value = []
    right_value = []

    if len(lst) <= 1:
        return lst
    else:
        key = lst[0]  # First number is a key.
        for i in lst:
            if i < key:
                left_value.append(i) 
                # print("Now_left: ",left_value)
            elif i > key:
                right_value.append(i) 
                # print("Now_right: ",right_value)
            else:
                key_value.append(i) 
                # print("KEY: ",key_value)

    left_value = quick_sort(left_value)
    right_value = quick_sort(right_value)

    # print("Finally_left: ",left_value)
    # print("Finally_right: ",right_value)
    # print("KEY: ",key_value)
    # print("\n")
    # print("NOW_List: ",left_value + key_value + right_value)
    # print("\n")
    return left_value + key_value + right_value

if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11]
    print(quick_sort(mylist))

# First loop(mylist):
#    left_value = [9, 0, 3, 11]
#    right_value = [100, 55]
#    key_value = [20]
# [0, 3, 9, 11] + [20]   (<- Left loop calculated result with key_value)
# [55, 100] (<- Right loop calculated result with key_value )

# Second loop(left):
    # left_value = [0, 3]
    # right_value = [11]
    # key_value = [9]
# return [0, 3] + [9] + [11]
# return the result to the First loop(mylist)

# Third loop(left):
    # left_value = []
    # right_value = [3]
    # key_value = [0]
# Now : left_value = []
# return left_value + key_value + right_value = [] + [0] + [3] 
# return the result to the Second loop(left)

# Second loop(right):
    # left_value = [55]
    # right_value = []
    # key_value = [100]
# Now : right_value = []
# return left_value + key_value + right_value = [55] + [100] + []
# return the result to the First loop(mylist) 

# finally: [0, 3, 9, 11] + [20] + [55, 100]