def bucket_sort(lst):
    bucket = []
    for i in range(max(lst)+1):
        bucket.append(0)
    for data in lst:
        bucket[data] = bucket[data] + 1
        
    index = 0
    for i in range(len(bucket)):
        if bucket[i] != 0:
            for j in range(bucket[i]):
                lst[index] = i
                index += 1
    return lst
        
if __name__ == "__main__":
    mylist = [20, 9, 100, 0, 55, 3, 11, 1, 3, 9, 55, 100, 20, 11, 3]
    print(bucket_sort(mylist))