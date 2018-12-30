n = int(input())
test = []
for i in range(0,n):
    
    a = int(input())
    a_set = set(map(int,input().split()))
    b = int(input())
    b_set = set(map(int,input().split()))
    for element in a_set:
        if element in b_set:
            test.append(True)
        else:
            test.append(False)
    
print(test)

