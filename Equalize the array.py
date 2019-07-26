'''
import statistics as st
n =  int(input())
temp = list(map(int,input().split()))
arr= sorted(temp)
#print(len(arr))
count = 0
try:
    m = st.mode(arr)
except st.StatisticsError as e:
    print(n-1)
else:
    for i in range(n):
        if(arr[i] != m):
            del[i]
            count += 1
    print(count)
    print(m)
    
# this code doesn't work for list with all unique elements
'''


n = int(input())
lst = list(map(int,input().split()))
print(n  - max([lst.count(i) for i in set(lst)]))