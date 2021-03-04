# Bubble sort
def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# Cocktail Sort
def cocktail_sort(lst):
    n = len(lst)
    is_sorted = True
    start = 0
    end = n - 1
    while is_sorted:
        # 向後排序
        is_sorted = False
        for i in range(start, end):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = True
        if not is_sorted:
            break
        end = end - 1

        # 向前排序
        for i in range(end-1, start-1, -1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = True
        start = start + 1

