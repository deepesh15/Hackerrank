x1,v1,x2,v2 = map(int,input().split())
if (x2>x1 and v2 >v1) or (v1 == v2):
    print("NO")
else:
    result = (x1-x2) % (v2-v1)
    if( result == 0):
        print("YES")
    else:
        print("NO")