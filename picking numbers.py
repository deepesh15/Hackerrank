n = int(input())
a = list(map(int,input().split()))
print(max(a.count(x)+a.count(x+1) for x in set(a)))