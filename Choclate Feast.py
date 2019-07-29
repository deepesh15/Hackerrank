n,c,m = list(map(int,input().split()))
wrappers = int(n/c)                             #number of choclate bars 
'''
ce = noc                                   #choclates eaten
while noc!=0:
    noc = noc/m
    ce += noc

print(ce)
'''
chocs = wrappers
while(wrappers >= m):
    wrappers -=m
    chocs +=1
    wrappers +=1
print(chocs)