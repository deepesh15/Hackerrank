def quicksort(arr):
    left, equal, right = [], [], []
    pivot = arr[0]
    for i in arr:
        if i == pivot:
            equal.append(i) 
        elif i > pivot:
            right.append(i) 
        elif i < pivot:
            left.append(i) 
    if len(left) > 1:
        left = quicksort(left)
    if len(right) > 1:
        right = quicksort(right)
    return left + equal + right

#quicksort partition
n = int(input())
lst = list(input().split())
for i in quicksort(lst):
    print(i,end=" ")
