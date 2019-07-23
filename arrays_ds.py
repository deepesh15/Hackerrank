n = int(input())
lst = list(map(int,input().strip().split()))
lst.reverse()
for i in range(len(lst)):
    print(lst[i],end=" ")