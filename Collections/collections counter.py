from collections import Counter

x = int(input())
sizes = list(map(int,input().split()))
total =0
for i in  range(int(input())):
    inpt = str(input())
    coun = Counter(sizes)
    size,amount = int(inpt[:inpt.index(" ")]),int(inpt[inpt.index(" "):])
    if size in coun.keys():
        total += amount
        sizes.remove(size)
        print(sizes)
        
    
print(total)
