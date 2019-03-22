n,k = map(int,input().split())
lst = list(map(int,input().split()))
sum_list = []
lst.sort()
count =0
for i in lst:
    for j in lst:
            if(i<j):
                sum_list.append(i+(j))
for i in sum_list:
    if(i%k == 1):
        count+=1


print(count)

'''
n,k = (int(x) for x in input().split())
lst = list(map(int, input().split()))

count = 0
for i in range(len(lst)-1):
    for x in range(1+i, len(lst)):     
        if (lst[i] + lst[x]) % k == 0:
            count += 1
        
print(count)
'''