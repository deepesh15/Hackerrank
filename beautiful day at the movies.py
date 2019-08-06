i,j,k = map(int,input().split())
print(sum((x-int(str(x)[::-1]))%k==0 for x in range(i,j+1)))