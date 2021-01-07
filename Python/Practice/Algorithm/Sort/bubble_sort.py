def bubble_sort(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[i] < lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11]
    print(bubble_sort(mylist))