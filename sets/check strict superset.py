set_A = set(map(int,input().split()))
literal = False
for _ in range(int(input())):
    set_B = set(map(int,input().split()))
    if set_A.issubset(set_B) and len(set_B)<len(set_A):
        literal =True
    
print(literal)