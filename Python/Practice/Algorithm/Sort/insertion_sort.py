def insertion_sort(lst):
    for i in range(1,len(lst)):
        tmp = lst[i]
        j = i - 1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = tmp
    return lst

if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11]
    print(insertion_sort(mylist))