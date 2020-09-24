def linear_serach(lst,t):
    for count in range(len(lst)):
        if lst[count] == t:
            return 'Element t is in the ' + str(count+1) + ' position of the list'
    return "Element t is not in the list"

if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11, 47, 33, 10, 88, 49]
    s = linear_serach(mylist,66)
    print(s)
# search time: Max: n; min: 1; avg: n