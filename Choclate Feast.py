n,c,m = list(map(int,input().split()))
wrappers = int(n/c)                             #number of choclate bars 
chocs = wrappers
while(wrappers >= m):
    wrappers -=m
    chocs +=1
    wrappers +=1
print(chocs)