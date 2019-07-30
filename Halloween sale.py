p,d,m,s = list(map(int,input().split()))
gb  =0
while s>=0:
    s -=p
    p = max(p-d,m)
    gb+=1
print(gb-1)

''' 
old logic failed at 100 99 81 180 
while s >= p:
    if p <= m:
        p=m
        s = s-p
        gb = gb+1
    else:
        s = s-p
        p = p -d
        gb = gb+1
print(gb)
'''
