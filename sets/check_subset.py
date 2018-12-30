n = int(input())
for i in range(0,n):
    
    a = int(input())
    a_set = set(map(int,input().split()))
    b = int(input())
    b_set = set(map(int,input().split()))
    print(a_set.issubset(b_set))
    

