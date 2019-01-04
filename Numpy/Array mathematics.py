import numpy 
n,m = map(int,input().split())
lstA = []
lstB = []
for _ in range(n):
    lstA.append(list(map(int,input().split())))

for _ in range(n):
    lstB.append(list(map(int,input().split())))

a = numpy.array(lstA)
b = numpy.array(lstB)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)