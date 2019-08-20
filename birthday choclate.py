n = int(input())
choc = list(map(int,input().split()))
d,m = list(map(int,input().split()))
print( sum(sum(choc[i:i+m])==d for i in range (n-m+1)))