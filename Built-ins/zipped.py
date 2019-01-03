n, x = map(int,input().split())
lst =[]
for _ in range(x):
    lst.append( map(float,input().split()))
for i in zip(*lst):
    print(sum(i)/len(i))