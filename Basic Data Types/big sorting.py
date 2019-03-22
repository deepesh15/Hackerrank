#big Sorting
n = int(input())
unsorted =[]
for _ in range(n):
    item=(int(input()))
    unsorted.append(item)
unsorted.sort()
for i in range(n):
    print(unsorted[i])