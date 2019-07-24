n = int(input())                            # size of the array
sticks =list(map(int,input().split()))      # each value represents ith length of the stick
print(len(sticks))
while True:
    sticks = [i for i in sticks if i!=min(sticks) ]
    if len(sticks) == 0:
        break
    print(len(sticks))

'''
print(len(arr))
while True:                 
    arr = [x for x in arr if x != min(arr)] 
    if len(arr)==0:
        break
    print(len(arr))
'''